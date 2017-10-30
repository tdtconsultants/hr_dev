# -*- coding: utf-8 -*-
from odoo import http

# class InterpodPartners(http.Controller):
#     @http.route('/interpod_partners/interpod_partners/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_partners/interpod_partners/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_partners.listing', {
#             'root': '/interpod_partners/interpod_partners',
#             'objects': http.request.env['interpod_partners.interpod_partners'].search([]),
#         })

#     @http.route('/interpod_partners/interpod_partners/objects/<model("interpod_partners.interpod_partners"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_partners.object', {
#             'object': obj
#         })