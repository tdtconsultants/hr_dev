# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class HREntryChecklist(models.Model):
    _name = 'hr.entry.checklist'
    _description = 'Employee Checklist'

    name = fields.Char(required="True")
    description = fields.Text()

class HRExitChecklist(models.Model):
    _name = 'hr.exit.checklist'
    _description = 'Employee Exit Checklist'

    name = fields.Char(required="True")
    description = fields.Text()

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    entry_checklist = fields.Many2many('hr.entry.checklist', 'employee_checklist_rel', 'checklist_id', 'employee_id', 'Entry Checklist', default=0.0)
    exit_checklist = fields.Many2many('hr.exit.checklist', 'exit_checklist_rel', 'checklist_id', 'employee_id', 'Exit Checklist', default=0.0)
    check_marked = fields.Float('Entry Progress', compute='_compute_check_marked',store=True)
    check_exit_marked = fields.Float('Exit Progress', compute='_compute_check_exit_marked',store=True)
    max_exit_value = fields.Float(compute='_get_max_exit_count', default=0.0)
    max_value = fields.Float(default=100.0)

    def _get_max_exit_count(self):
        for rec in self:
            all_checklist = self.env['hr.exit.checklist'].search([])
            rec.max_exit_value = len(all_checklist)

    @api.depends('entry_checklist')
    def _compute_check_marked(self):
        all_checklist = self.env['hr.entry.checklist'].search([])
        if len(all_checklist) >=1 :
            for rec in self:
                selected_checklist = rec.entry_checklist
                rec.check_marked = (len(selected_checklist)* 100)/len(all_checklist)

    @api.depends('exit_checklist')
    def _compute_check_exit_marked(self):
        all_checklist = self.env['hr.exit.checklist'].search([])
        if len(all_checklist) >=1 :
            for rec in self:
                selected_checklist = rec.exit_checklist
                rec.check_exit_marked = (len(selected_checklist)* 100)/len(all_checklist)

    @api.multi
    def toggle_active(self):
        """ Inverse the value of the field ``active`` on the records in ``self``. """
        for record in self:
            if record.active and record.check_exit_marked != 100:
                raise ValidationError(_('Please complete exit procedure first, It is competed only %s %% yet.') % record.check_exit_marked)
            record.active = not record.active
