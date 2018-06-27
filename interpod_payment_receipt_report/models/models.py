# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_is_zero


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    credit_applied = fields.Monetary(
        string="Credit Applied",
        help="Credit applied to the invoice",
        compute='_get_credit_applied')
    payment = fields.Monetary(
        string="Payment",
        help="Payment, not counting credit notes",
        compute='_get_payment')

    @api.one
    @api.depends('credit_applied')
    def _get_payment(self):
        """Compute the amount paid w/o credit notes"""
        self.payment = self.amount_total - self.credit_applied - self.residual

    @api.one
    def _get_credit_applied(self):
        """Compute the amount of credit applied"""
        payments = self._get_payments()
        self.credit_applied = sum(
            i['amount']
            for i in payments
            if i['payment_id'].journal_id.type == 'purchase')

    def _get_payments(self):
        """Get payments associated with an invoice"""
        payments = []
        for payment in self.payment_move_line_ids:
            if self.type in ('out_invoice', 'in_refund'):
                movs, move_id = payment.matched_debit_ids, lambda p: p.debit_move_id
            elif self.type in ('in_invoice', 'out_refund'):
                movs, move_id = payment.matched_credit_ids, lambda p: p.credit_move_id
            if movs and all(p.currency_id == self.currency_id for p in movs):
                amount_currency = sum(p.amount_currency for p in movs if move_id(p) in self.move_id.line_ids)
                amount_to_show = amount_currency
            else:
                amount = sum(p.amount for p in movs if move_id(p) in self.move_id.line_ids)
                amount_to_show = payment.company_id \
                    .currency_id.with_context(date=self.date) \
                    .compute(amount, self.currency_id)
            if float_is_zero(amount_to_show, precision_rounding=self.currency_id.rounding):
                continue
            payments.extend([{
                'amount': amount_to_show,
                'currency_id': self.currency_id,
                'payment_id': payment,
            }])
        return payments
