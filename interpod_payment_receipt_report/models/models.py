# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class interpod_payment_receipt_report(models.Model):
#     _name = 'interpod_payment_receipt_report.interpod_payment_receipt_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100