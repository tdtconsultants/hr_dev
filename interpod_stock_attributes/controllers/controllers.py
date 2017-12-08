# -*- coding: utf-8 -*-
from odoo import http

# class InterpodStockAttributes(http.Controller):
#     @http.route('/interpod_stock_attributes/interpod_stock_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_stock_attributes/interpod_stock_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_stock_attributes.listing', {
#             'root': '/interpod_stock_attributes/interpod_stock_attributes',
#             'objects': http.request.env['interpod_stock_attributes.interpod_stock_attributes'].search([]),
#         })

#     @http.route('/interpod_stock_attributes/interpod_stock_attributes/objects/<model("interpod_stock_attributes.interpod_stock_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_stock_attributes.object', {
#             'object': obj
#         })