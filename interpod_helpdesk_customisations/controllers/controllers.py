# -*- coding: utf-8 -*-
from odoo import http

# class InterpodHelpdeskCustomisations(http.Controller):
#     @http.route('/interpod_helpdesk_customisations/interpod_helpdesk_customisations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_helpdesk_customisations/interpod_helpdesk_customisations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_helpdesk_customisations.listing', {
#             'root': '/interpod_helpdesk_customisations/interpod_helpdesk_customisations',
#             'objects': http.request.env['interpod_helpdesk_customisations.interpod_helpdesk_customisations'].search([]),
#         })

#     @http.route('/interpod_helpdesk_customisations/interpod_helpdesk_customisations/objects/<model("interpod_helpdesk_customisations.interpod_helpdesk_customisations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_helpdesk_customisations.object', {
#             'object': obj
#         })