from openerp import models, api, fields, _

class Product(models.Model):
    _inherit = "product.template"

    #name = fields.Char('Name', index=True, required=True)
    interpod_product_projects = fields.Many2many('project.project', string = "Project(s)", relation = 'product_template_project_project_rel' ,required = False, translate = False)


class ProductProduct(models.Model):

    _inherit = "product.product"
    interpod_product_projects = fields.Many2many('project.project', string = "Project", related = 'product_tmpl_id.interpod_product_projects', required = False, store = False, translate = False)
