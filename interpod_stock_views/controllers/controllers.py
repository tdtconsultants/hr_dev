# -*- coding: utf-8 -*-
from odoo import http

# class InterpodStockViews(http.Controller):
#     @http.route('/interpod_stock_views/interpod_stock_views/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_stock_views/interpod_stock_views/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_stock_views.listing', {
#             'root': '/interpod_stock_views/interpod_stock_views',
#             'objects': http.request.env['interpod_stock_views.interpod_stock_views'].search([]),
#         })

#     @http.route('/interpod_stock_views/interpod_stock_views/objects/<model("interpod_stock_views.interpod_stock_views"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_stock_views.object', {
#             'object': obj
#         })