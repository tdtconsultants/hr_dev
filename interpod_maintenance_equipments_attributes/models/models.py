# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class interpod_maintenance_equipments_attributes(models.Model):
#     _name = 'interpod_maintenance_equipments_attributes.interpod_maintenance_equipments_attributes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100