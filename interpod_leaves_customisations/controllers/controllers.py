# -*- coding: utf-8 -*-
from odoo import http

# class InterpodLeavesCustomisations(http.Controller):
#     @http.route('/interpod_leaves_customisations/interpod_leaves_customisations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_leaves_customisations/interpod_leaves_customisations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_leaves_customisations.listing', {
#             'root': '/interpod_leaves_customisations/interpod_leaves_customisations',
#             'objects': http.request.env['interpod_leaves_customisations.interpod_leaves_customisations'].search([]),
#         })

#     @http.route('/interpod_leaves_customisations/interpod_leaves_customisations/objects/<model("interpod_leaves_customisations.interpod_leaves_customisations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_leaves_customisations.object', {
#             'object': obj
#         })