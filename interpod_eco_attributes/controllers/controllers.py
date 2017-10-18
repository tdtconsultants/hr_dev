# -*- coding: utf-8 -*-
from odoo import http

# class InterpodEcoAttributes(http.Controller):
#     @http.route('/interpod_eco_attributes/interpod_eco_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_eco_attributes/interpod_eco_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_eco_attributes.listing', {
#             'root': '/interpod_eco_attributes/interpod_eco_attributes',
#             'objects': http.request.env['interpod_eco_attributes.interpod_eco_attributes'].search([]),
#         })

#     @http.route('/interpod_eco_attributes/interpod_eco_attributes/objects/<model("interpod_eco_attributes.interpod_eco_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_eco_attributes.object', {
#             'object': obj
#         })