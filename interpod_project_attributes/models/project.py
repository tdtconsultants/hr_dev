from openerp import models, api, fields, _

class Project(models.Model):
    _inherit = "project.project"

    #name = fields.Char('Name', index=True, required=True)
    interpod_project_site = fields.Char(required = False, translate = False)


class ProjectTask(models.Model):
    _inherit = "project.task"

    description_pad = fields.Char('Pad URL', required=False)
