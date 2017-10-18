# -*- coding: utf-8 -*-
from odoo import http

# class InterpodInvoiceAttributes(http.Controller):
#     @http.route('/interpod_invoice_attributes/interpod_invoice_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_invoice_attributes/interpod_invoice_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_invoice_attributes.listing', {
#             'root': '/interpod_invoice_attributes/interpod_invoice_attributes',
#             'objects': http.request.env['interpod_invoice_attributes.interpod_invoice_attributes'].search([]),
#         })

#     @http.route('/interpod_invoice_attributes/interpod_invoice_attributes/objects/<model("interpod_invoice_attributes.interpod_invoice_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_invoice_attributes.object', {
#             'object': obj
#         })