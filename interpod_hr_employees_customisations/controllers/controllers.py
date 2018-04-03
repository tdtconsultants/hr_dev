# -*- coding: utf-8 -*-
from odoo import http

# class InterpodHrEmployeesCustomisations(http.Controller):
#     @http.route('/interpod_hr_employees_customisations/interpod_hr_employees_customisations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interpod_hr_employees_customisations/interpod_hr_employees_customisations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interpod_hr_employees_customisations.listing', {
#             'root': '/interpod_hr_employees_customisations/interpod_hr_employees_customisations',
#             'objects': http.request.env['interpod_hr_employees_customisations.interpod_hr_employees_customisations'].search([]),
#         })

#     @http.route('/interpod_hr_employees_customisations/interpod_hr_employees_customisations/objects/<model("interpod_hr_employees_customisations.interpod_hr_employees_customisations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interpod_hr_employees_customisations.object', {
#             'object': obj
#         })