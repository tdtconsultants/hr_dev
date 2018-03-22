# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit= 'product.template'

    generic_consumable = fields.Boolean(help="Tick if you want this product to generate analytic lines when processing a work order that uses this kind of product")

class ManufacturingOrder(models.Model):

    _inherit = "mrp.production"

    analytic_account_id = fields.Many2one('account.analytic.account', help="Generic consumables will generate analytic lines in this account")

class InvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.model
    def create(self, vals):
        if vals['account_analytic_id']:
            prod = self.env['product.product'].browse(vals['product_id'])
            if prod.product_tmpl_id.generic_consumable:
                raise UserError("You cannot set an analytic account on a generic consumable product, you must set it later on the Manufacturing order")
        line = super(InvoiceLine, self).create(vals)
        return line



class WorkOrder(models.Model):

    _inherit = "mrp.workorder"

    def record_production(self):
        res = super(WorkOrder, self).record_production()
        self.generate_analytic_lines()
        return res

    def generate_analytic_lines(self):
        """
        Generates analytic lines to register the consumed generic consumables expenses to the manufacturing order's analytic account
        """
        analytic_account = self.production_id.analytic_account_id
        for stock_move in self.move_raw_ids:
            for stock_move_line in stock_move.move_line_ids:
                qty_done = stock_move_line.qty_done
                product = stock_move_line.product_id
                product_tmpl = product.product_tmpl_id
                if qty_done > 0 and product_tmpl.generic_consumable:
                    if not analytic_account:
                        raise UserError("If this work order consumes generic consumable products the manufacturing order must have an analytic account assigned")
                    amount = qty_done * product_tmpl.standard_price
                    self.env['account.analytic.line'].create({
                        'name': self.production_id.name,
                        'ref': self.production_id.name,
                        'account_id': analytic_account.id,
                        'amount': amount,
                        'date': datetime.now(),
                        'product_id': product.id,
                        'unit_amount': qty_done
                    })
