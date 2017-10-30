# -*- coding: utf-8 -*-
from odoo import http

# class InterpodIrViews(http.Controller):
#     @http.route('/interpod_ir_views/interpod_ir_views/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_ir_views/interpod_ir_views/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_ir_views.listing', {
#             'root': '/interpod_ir_views/interpod_ir_views',
#             'objects': http.request.env['interpod_ir_views.interpod_ir_views'].search([]),
#         })

#     @http.route('/interpod_ir_views/interpod_ir_views/objects/<model("interpod_ir_views.interpod_ir_views"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_ir_views.object', {
#             'object': obj
#         })