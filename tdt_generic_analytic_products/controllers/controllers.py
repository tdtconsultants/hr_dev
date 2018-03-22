# -*- coding: utf-8 -*-
from odoo import http

# class TdtGenericAnalyticProducts(http.Controller):
#     @http.route('/tdt_generic_analytic_products/tdt_generic_analytic_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdt_generic_analytic_products/tdt_generic_analytic_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdt_generic_analytic_products.listing', {
#             'root': '/tdt_generic_analytic_products/tdt_generic_analytic_products',
#             'objects': http.request.env['tdt_generic_analytic_products.tdt_generic_analytic_products'].search([]),
#         })

#     @http.route('/tdt_generic_analytic_products/tdt_generic_analytic_products/objects/<model("tdt_generic_analytic_products.tdt_generic_analytic_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdt_generic_analytic_products.object', {
#             'object': obj
#         })
