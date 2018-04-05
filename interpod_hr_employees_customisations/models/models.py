# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):

    _inherit = "hr.employee"

    personal_phone = fields.Char()
    
    @api.multi
    def write(self, vals):
        if 'related_partner_id' in vals:
            partner = self.env['res.partner'].browse(vals['related_partner_id'])
            partner._compute_is_employee()
        if 'user_id' in vals:
            partner = self.env['res.users'].browse(vals['user_id']).partner_id
            partner._compute_is_employee()
        return super(Employee, self).write(vals)
    

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    related_partner_id = fields.Many2one('res.partner', compute='_compute_related_partner', store=True)


class Partner(models.Model):

    _inherit = "res.partner"

    @api.one
    def _compute_is_employee(self):
        if self.employee:
            return True
        employee = self.env['hr.employee'].search([('related_partner_id','=', self.id)])
        self.is_employee = True if employee else False
        
    is_employee = fields.Boolean(compute="_compute_is_employee", store=True)

    def compute_all_is_employee(self):
        partners = self.env['res.partner'].search([])
        partners.mapped(lambda p: p._compute_is_employee())

