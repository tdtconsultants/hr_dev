# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    credit_applied = fields.Monetary(
        string="Credit Applied",
        help="Credit applied to the invoice",
        compute='_get_credit_total',
    )
    payment = fields.Monetary(
        string="Payment",
        help="Payment, not counting credit notes",
        compute='_get_payment',
    )
    credit_payment_id = fields.Many2many(
        'account.move.line',
        string="Payments from Credit Notes",
        compute="_get_credit_list",
    )

    @api.one
    @api.depends('credit_applied')
    def _get_payment(self):
        """Compute the amount paid w/o credit notes"""
        self.payment = self.amount_total - self.credit_applied - self.residual

    @api.one
    def _get_credit_total(self):
        """Compute the amount of credit applied"""
        self.credit_applied = sum(
            self.credit_payment_id
            .mapped('matched_credit_ids')
            .filtered(lambda c: c.credit_move_id in self.move_id.line_ids)
            .mapped(lambda m: m.currency_amount
                    if m.currency_id == self.currency_id
                    else m.company_currency_id
                    .with_context(date=self.date)
                    .compute(m.amount, self.currency_id)
            )
        )

    @api.one
    def _get_credit_list(self):
        self.credit_payment_id = self.payment_move_line_ids \
            .filtered(lambda payment: payment.journal_id.type == 'purchase')
