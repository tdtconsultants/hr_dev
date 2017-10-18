# -*- coding: utf-8 -*-
from odoo import http

# class InterpodQualityAlertsAttributes(http.Controller):
#     @http.route('/interpod_quality_alerts_attributes/interpod_quality_alerts_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_quality_alerts_attributes/interpod_quality_alerts_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_quality_alerts_attributes.listing', {
#             'root': '/interpod_quality_alerts_attributes/interpod_quality_alerts_attributes',
#             'objects': http.request.env['interpod_quality_alerts_attributes.interpod_quality_alerts_attributes'].search([]),
#         })

#     @http.route('/interpod_quality_alerts_attributes/interpod_quality_alerts_attributes/objects/<model("interpod_quality_alerts_attributes.interpod_quality_alerts_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_quality_alerts_attributes.object', {
#             'object': obj
#         })