# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def action_invoice_open(self):
        for invoice in self:
            if invoice.amount_total == 0:
                raise UserError("Invoice with a total amount of $0 can't be validated.")
        return super(AccountInvoice, self).action_invoice_open()

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        for so in self:
            if so.amount_total == 0:
                raise UserError("Sale Order with a total amount of $0 can't be validated.")
        return super(SaleOrder, self).action_confirm()
