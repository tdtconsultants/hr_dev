# -*- coding: utf-8 -*-

from odoo import models, fields, api

class interpod_stock_attributes(models.Model):
     _inherit = 'stock.picking'
     is_locked = fields.Boolean(default=False, help='When the picking is not done this allows changing the initial demand. When the picking is done this allows changing the done quantities.')
