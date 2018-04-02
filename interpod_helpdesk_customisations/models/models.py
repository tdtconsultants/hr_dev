# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    user_id = fields.Many2one('res.users', string='Assigned to', track_visibility='onchange', domain=[])


