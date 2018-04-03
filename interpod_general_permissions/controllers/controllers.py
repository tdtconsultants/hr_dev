# -*- coding: utf-8 -*-
from odoo import http

# class InterpodGeneralPermissions(http.Controller):
#     @http.route('/interpod_general_permissions/interpod_general_permissions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_general_permissions/interpod_general_permissions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_general_permissions.listing', {
#             'root': '/interpod_general_permissions/interpod_general_permissions',
#             'objects': http.request.env['interpod_general_permissions.interpod_general_permissions'].search([]),
#         })

#     @http.route('/interpod_general_permissions/interpod_general_permissions/objects/<model("interpod_general_permissions.interpod_general_permissions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_general_permissions.object', {
#             'object': obj
#         })