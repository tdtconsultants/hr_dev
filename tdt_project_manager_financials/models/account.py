from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "account.account"

    project_manager_access = fields.Boolean(
        string='Project manager access',
        help="When active, a project manager will have reading access to journal items in this account.", default=False)
