from odoo import models, fields

class AnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    project_manager_access = fields.Boolean(
        string='Project manager access',
        help="When active, a project manager will have reading access to the entries in this account.", default=False)
