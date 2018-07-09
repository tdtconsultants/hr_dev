from openerp import models, api, fields, _

class Product(models.Model):
    _inherit = "product.template"

    sale_ok = fields.Boolean(
         'Can be Sold',
         default=False,
         help="Specify if the product can be selected in a sales order line.",
    )
    interpod_product_projects = fields.Many2many(
        'project.project',
        string="Project(s)",
        relation='product_template_project_project_rel',
        required=False,
        translate=False
    )


class ProductProduct(models.Model):
    _inherit = "product.product"

    interpod_product_projects = fields.Many2many(
        'project.project',
        string="Project",
        related='product_tmpl_id.interpod_product_projects',
        required=False,
        store=False,
        translate=False
    )
