# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    user_id = fields.Many2one('res.users', string='Assigned to', track_visibility='onchange', domain=[])

    partner_id = fields.Many2one('res.partner', string='Customer', domain=[('is_employee','=',True)])

    team_id = fields.Many2one('helpdesk.team', string='Helpdesk Team', default=None, index=True, required=True)
    true_field = fields.Boolean(default=True, readonly=True)

    current_behaviour = fields.Text()
    expected_behaviour = fields.Text()
    steps_to_reproduce = fields.Text(help="Detailed steps and context to reproduce this error/unwanted behaviour")


    @api.model
    def create(self, vals):
        if not vals.get('partner_id'):
            vals['partner_id'] = self.env.user.partner_id.id
        return super(HelpdeskTicket, self).create(vals)

class User(models.Model):
    _inherit = 'res.users'

    @api.one
    def _compute_is_helpdesk_user(self):
        try:
            group = self.env.ref('helpdesk.group_helpdesk_user')
        except Exception:
            raise UserError('External ID of group: "helpdesk.group_helpdesk_user" not found')
        self.is_helpdesk_user = group.id in self.groups_id.ids

    is_helpdesk_user = fields.Boolean(compute='_compute_is_helpdesk_user', store=True)
