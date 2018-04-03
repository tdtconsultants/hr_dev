# -*- coding: utf-8 -*-

from odoo import models, fields, api

class interpod_hr_employees_customisations(models.Model):

    _inherit = "hr.employee"

    personal_phone = fields.Char()

