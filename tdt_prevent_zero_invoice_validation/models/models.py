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


