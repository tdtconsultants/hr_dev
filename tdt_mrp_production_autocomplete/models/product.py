from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    autocomplete_manufacturing_order = fields.Boolean(
        string='Autocomplete manufacturing order',
        help="When active, a manufacturing order for this product will be automatically set to done when all its workorders are completed.")
