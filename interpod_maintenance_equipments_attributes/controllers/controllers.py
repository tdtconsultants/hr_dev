# -*- coding: utf-8 -*-
from odoo import http

# class InterpodMaintenanceEquipmentsAttributes(http.Controller):
#     @http.route('/interpod_maintenance_equipments_attributes/interpod_maintenance_equipments_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_maintenance_equipments_attributes/interpod_maintenance_equipments_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_maintenance_equipments_attributes.listing', {
#             'root': '/interpod_maintenance_equipments_attributes/interpod_maintenance_equipments_attributes',
#             'objects': http.request.env['interpod_maintenance_equipments_attributes.interpod_maintenance_equipments_attributes'].search([]),
#         })

#     @http.route('/interpod_maintenance_equipments_attributes/interpod_maintenance_equipments_attributes/objects/<model("interpod_maintenance_equipments_attributes.interpod_maintenance_equipments_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_maintenance_equipments_attributes.object', {
#             'object': obj
#         })