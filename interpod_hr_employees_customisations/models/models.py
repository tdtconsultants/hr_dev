# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)



class Employee(models.Model):

    _inherit = "hr.employee"

    personal_phone = fields.Char()
    related_partner_id = fields.Many2one('res.partner', compute='_compute_related_partner', store=True)

    nok_name = fields.Char()
    nok_contact = fields.Char()

    @api.one
    def _compute_related_partner(self):
        self.related_partner_id = self.user_id.partner_id


    @api.model
    def create(self, vals):
        if 'user_id' in vals:
            if vals['user_id']:
                partner = self.env['res.users'].browse(vals['user_id']).partner_id
                partner.is_employee = True
        return super(Employee, self).create(vals)

 
    @api.multi
    def write(self, vals):
        if 'user_id' in vals:
            if not vals['user_id']:
                ### we lost reference to the partner id so we compute all
                res = super(Employee, self).write(vals)
                self.env['res.partner'].compute_all_is_employee()
                return res
            else:
                partner = self.env['res.users'].browse(vals['user_id']).partner_id
                partner.is_employee = True
        return super(Employee, self).write(vals)

    def unlink(self):
        res = super(Employee, self).unlink()
        self.env['res.partner'].compute_all_is_employee()
        return res

class Partner(models.Model):

    _inherit = "res.partner"

    @api.one
    def _compute_is_employee(self):
        if self.employee:
            return True
        employee = self.env['hr.employee'].search(['|',('related_partner_id','=', self.id),('user_id.partner_id','=',self.id)])
        self.is_employee = True if employee else False
        
    is_employee = fields.Boolean(compute="_compute_is_employee", store=True)

    def compute_all_is_employee(self):
        partners = self.env['res.partner'].search([])
        for p in partners:
            p._compute_is_employee()
