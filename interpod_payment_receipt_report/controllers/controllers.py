# -*- coding: utf-8 -*-
from odoo import http

# class InterpodPaymentReceiptReport(http.Controller):
#     @http.route('/interpod_payment_receipt_report/interpod_payment_receipt_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_payment_receipt_report/interpod_payment_receipt_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_payment_receipt_report.listing', {
#             'root': '/interpod_payment_receipt_report/interpod_payment_receipt_report',
#             'objects': http.request.env['interpod_payment_receipt_report.interpod_payment_receipt_report'].search([]),
#         })

#     @http.route('/interpod_payment_receipt_report/interpod_payment_receipt_report/objects/<model("interpod_payment_receipt_report.interpod_payment_receipt_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_payment_receipt_report.object', {
#             'object': obj
#         })