from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    autocomplete_manufacturing_order = fields.Boolean(
        string='Autocomplete manufacturing order',
        help="If this option is active on this product,"
        "when all the work orders of a manufacturing order for this product are completed, the manufacturing order will automatically be set to ready."
        )
