# -*- coding: utf-8 -*-
from odoo import http

# class InterpodDrawdownViews(http.Controller):
#     @http.route('/interpod_drawdown_views/interpod_drawdown_views/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_drawdown_views/interpod_drawdown_views/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_drawdown_views.listing', {
#             'root': '/interpod_drawdown_views/interpod_drawdown_views',
#             'objects': http.request.env['interpod_drawdown_views.interpod_drawdown_views'].search([]),
#         })

#     @http.route('/interpod_drawdown_views/interpod_drawdown_views/objects/<model("interpod_drawdown_views.interpod_drawdown_views"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_drawdown_views.object', {
#             'object': obj
#         })