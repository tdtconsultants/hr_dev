# -*- coding: utf-8 -*-
from odoo import http

# class InterpodProjectAttributes(http.Controller):
#     @http.route('/interpod_project_attributes/interpod_project_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_project_attributes/interpod_project_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_project_attributes.listing', {
#             'root': '/interpod_project_attributes/interpod_project_attributes',
#             'objects': http.request.env['interpod_project_attributes.interpod_project_attributes'].search([]),
#         })

#     @http.route('/interpod_project_attributes/interpod_project_attributes/objects/<model("interpod_project_attributes.interpod_project_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_project_attributes.object', {
#             'object': obj
#         })