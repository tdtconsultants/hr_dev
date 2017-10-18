# -*- coding: utf-8 -*-

from odoo import models, fields, api

class test_module(models.Model):
    _inherit = 'res.partner'


    def import_imgs(self):
        path = '/home/cado/contacts_imgs.csv'
        csv = open(path, 'r')
        keep_reading = True
        import pdb;pdb.set_trace()
        while keep_reading:
            line = csv.readline()
            if line:
                vals = line.split(',')
                self.env['res.partner'].browse(int(vals[1])).image = line[2]
            else:
                break
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
