# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    user_id = fields.Many2one('res.users', string='Assigned to', track_visibility='onchange', domain=[])

    @api.model
    def create(self, vals):
        if not vals.get('partner_id'):
            vals['partner_id'] = self.env.user.partner_id.id
        return super(HelpdeskTicket, self).create(vals)
