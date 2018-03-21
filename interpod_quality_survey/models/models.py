# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    survey_id = fields.Many2one('survey.survey', string="Survey", help="Survey for the final quality control")

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.production'

    location_id = fields.Char(help="Added to fix bug on views")
    survey_answer_id = fields.Many2one('survey.user_input', string="QC Survey Answer")

    @api.multi
    def show_qc_survey(self):
        return {
            'type': 'ir.actions.act_url',
            'name': "Results of the Survey",
            'target': 'self',
            'url': 'interpod_qc/' + self.product_id.product_tmpl_id.survey_id.with_context(relative_url=True).public_url + '/' + str(self.id)
        }

    @api.multi
    def button_mark_done(self):
        if self.survey_answer_id and self.survey_answer_id.state == 'done':
            return super(ManufacturingOrder, self).button_mark_done()
        else:
            raise UserError("You must complete the QC survey before marking this as done")

class SurveyAnswer(models.Model):
    _inherit = 'survey.user_input'

    manufacturing_order_ids = fields.One2many('mrp.production', 'survey_answer_id')
