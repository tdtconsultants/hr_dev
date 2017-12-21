# -*- coding: utf-8 -*-

from odoo import models, fields, api

class interpod_stock_attributes(models.Model):
     _inherit = 'stock.picking'
     is_locked = fields.Boolean(default=False, help='When the picking is not done this allows changing the initial demand. When the picking is done this allows changing the done quantities.')



class Location(models.Model):
    _inherit = "stock.location"
    _order = "parent_left, name"

    complete_name = fields.Char("Full Location Name", compute='_compute_complete_name', store=True, index=True)
    name = fields.Char('Location Name', required=True, translate=True, index=True)




class InventoryLine(models.Model):
    _inherit = "stock.inventory.line"
    _order = "location_name"
    location_name = fields.Char('Location Name', related='location_id.complete_name', store=True, index = True)

