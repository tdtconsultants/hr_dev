# -*- coding: utf-8 -*-
from odoo import http

# class InterpodProductAttributes(http.Controller):
#     @http.route('/interpod_product_attributes/interpod_product_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_product_attributes/interpod_product_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_product_attributes.listing', {
#             'root': '/interpod_product_attributes/interpod_product_attributes',
#             'objects': http.request.env['interpod_product_attributes.interpod_product_attributes'].search([]),
#         })

#     @http.route('/interpod_product_attributes/interpod_product_attributes/objects/<model("interpod_product_attributes.interpod_product_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_product_attributes.object', {
#             'object': obj
#         })