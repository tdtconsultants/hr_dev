# -*- coding: utf-8 -*-
#from addons.survey.controllers.main import WebsiteSurvey
import json
import logging

from odoo import fields, http, SUPERUSER_ID
from odoo.http import request
from odoo.tools import ustr

_logger = logging.getLogger(__name__)


class WebsiteSurvey(http.Controller):
    def _check_bad_cases(self, survey, token=None):
        # In case of bad survey, redirect to surveys list
        if not survey.sudo().exists():
            return werkzeug.utils.redirect("/survey/")

        # In case of auth required, block public user
        if survey.auth_required and request.env.user == request.website.user_id:
            return request.render("survey.auth_required", {'survey': survey, 'token': token})

        # In case of non open surveys
        if survey.stage_id.closed:
            return request.render("survey.notopen")

        # If there is no pages
        if not survey.page_ids:
            return request.render("survey.nopages", {'survey': survey})

        # Everything seems to be ok
        return None

    def _check_deadline(self, user_input):
        '''Prevent opening of the survey if the deadline has turned out

        ! This will NOT disallow access to users who have already partially filled the survey !'''
        deadline = user_input.deadline
        if deadline:
            dt_deadline = fields.Datetime.from_string(deadline)
            dt_now = datetime.now()
            if dt_now > dt_deadline:  # survey is not open anymore
                return request.render("survey.notopen")
        return None


    # Survey start
    @http.route(['/interpod_qc/survey/start/<model("survey.survey"):survey>/<string:mo_id>',
                 '/interpod_qc/survey/start/<model("survey.survey"):survey>/<string:token>/<string:mo_id>'],
                type='http', auth='public', website=True)
    def start_survey(self, survey, mo_id = None, token=None, **post):
        UserInput = request.env['survey.user_input']
        # Test mode
        if token and token == "phantom":
            _logger.info("[survey] Phantom mode")
            user_input = UserInput.create({'survey_id': survey.id, 'test_entry': True})
            data = {'survey': survey, 'page': None, 'token': user_input.token, 'mo_id':mo_id}
            return request.render('survey.survey_init', data)
        # END Test mode

        # Controls if the survey can be displayed
        errpage = self._check_bad_cases(survey, token=token)
        if errpage:
            return errpage

        # Manual surveying
        if not token:
            vals = {'survey_id': survey.id}
            if request.website.user_id != request.env.user:
                vals['partner_id'] = request.env.user.partner_id.id
            user_input = UserInput.create(vals)
        else:
            user_input = UserInput.sudo().search([('token', '=', token)], limit=1)
            if not user_input:
                return request.render("website.403")

        # Do not open expired survey
        errpage = self._check_deadline(user_input)
        if errpage:
            return errpage

        # Select the right page
        if user_input.state == 'new':  # Intro page
            data = {'survey': survey, 'page': None, 'token': user_input.token, 'mo_id':mo_id}
            return request.render('survey.survey_init', data)
        else:
            return request.redirect('/survey/fill/%s/%s' % (survey.id, user_input.token))

    # Survey displaying
    @http.route(['/interpod_qc/survey/fill/<model("survey.survey"):survey>/<string:token>/<string:mo_id>',
                 '/interpod_qc/survey/fill/<model("survey.survey"):survey>/<string:token>/<string:mo_id>/<string:prev>'],
                type='http', auth='public', website=True)
    def fill_survey(self, survey, token, mo_id=None, prev=None, **post):
        '''Display and validates a survey'''
        Survey = request.env['survey.survey']
        UserInput = request.env['survey.user_input']
        # Controls if the survey can be displayed
        errpage = self._check_bad_cases(survey)
        if errpage:
            return errpage

        # Load the user_input
        user_input = UserInput.sudo().search([('token', '=', token)], limit=1)
        if not user_input:  # Invalid token
            return request.render("website.403")

        # Do not display expired survey (even if some pages have already been
        # displayed -- There's a time for everything!)
        errpage = self._check_deadline(user_input)
        if errpage:
            return errpage

        # Select the right page
        if user_input.state == 'new':  # First page
            page, page_nr, last = Survey.next_page(user_input, 0, go_back=False)
            data = {'survey': survey, 'page': page, 'page_nr': page_nr, 'token': user_input.token, 'mo_id': mo_id }
            if last:
                data.update({'last': True, 'mo_id': mo_id})
            return request.render('survey.survey', data)
        elif user_input.state == 'done':  # Display success message
            return request.render('survey.sfinished', {'survey': survey,
                                                               'token': token,
                                                               'user_input': user_input,
                                                               'mo_id': mo_id })
        elif user_input.state == 'skip':
            flag = (True if prev and prev == 'prev' else False)
            page, page_nr, last = Survey.next_page(user_input, user_input.last_displayed_page_id.id, go_back=flag)

            #special case if you click "previous" from the last page, then leave the survey, then reopen it from the URL, avoid crash
            if not page:
                page, page_nr, last = Survey.next_page(user_input, user_input.last_displayed_page_id.id, go_back=True)

            data = {'survey': survey, 'page': page, 'page_nr': page_nr, 'token': user_input.token, 'mo_id':mo_id}
            if last:
                data.update({'last': True, 'mo_id':mo_id})
            return request.render('survey.survey', data)
        else:
            return request.render("website.403")

    # AJAX submission of a page
    @http.route(['/interpod_qc/survey/submit/<model("survey.survey"):survey>/<string:mo_id>'], type='http', methods=['POST'], auth='public', website=True)
    def submit(self, survey, mo_id=None, **post):
        _logger.debug('Incoming data: %s', post)
        page_id = int(post['page_id'])
        questions = request.env['survey.question'].search([('page_id', '=', page_id)])

        # Answer validation
        errors = {}
        for question in questions:
            answer_tag = "%s_%s_%s" % (survey.id, page_id, question.id)
            errors.update(question.validate_question(post, answer_tag))

        ret = {}
        if len(errors):
            # Return errors messages to webpage
            ret['errors'] = errors
        else:
            # Store answers into database
            try:
                user_input = request.env['survey.user_input'].sudo().search([('token', '=', post['token'])], limit=1)
            except KeyError:  # Invalid token
                return request.render("website.403")
            user_id = request.env.user.id if user_input.type != 'link' else SUPERUSER_ID

            for question in questions:
                answer_tag = "%s_%s_%s" % (survey.id, page_id, question.id)
                request.env['survey.user_input_line'].sudo(user=user_id).save_lines(user_input.id, question, post, answer_tag)

            go_back = post['button_submit'] == 'previous'
            next_page, _, last = request.env['survey.survey'].next_page(user_input, page_id, go_back=go_back)
            vals = {'last_displayed_page_id': page_id }
            if next_page is None and not go_back:
                vals.update({'state': 'done'})
                if mo_id and mo_id != 'None':
                    mo = request.env['mrp.production'].browse(int(mo_id))
                    survey_answer = request.env['survey.user_input'].browse(user_input.id)
                    mo.survey_answer_id = survey_answer.id
            else:
                vals.update({'state': 'skip'})
            user_input.sudo(user=user_id).write(vals)
            if not mo_id:
                mo_id = ''
            ret['redirect'] = '/interpod_qc/survey/fill/%s/%s/%s' % (survey.id, post['token'], str(mo_id))
            if go_back:
                ret['redirect'] += '/prev'
        return json.dumps(ret)
