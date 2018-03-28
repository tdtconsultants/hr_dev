# -*- coding: utf-8 -*-
from odoo import http

# class InterpodWorkOrderPlanning(http.Controller):
#     @http.route('/interpod_work_order_planning/interpod_work_order_planning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_work_order_planning/interpod_work_order_planning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_work_order_planning.listing', {
#             'root': '/interpod_work_order_planning/interpod_work_order_planning',
#             'objects': http.request.env['interpod_work_order_planning.interpod_work_order_planning'].search([]),
#         })

#     @http.route('/interpod_work_order_planning/interpod_work_order_planning/objects/<model("interpod_work_order_planning.interpod_work_order_planning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_work_order_planning.object', {
#             'object': obj
#         })