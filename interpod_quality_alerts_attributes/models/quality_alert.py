from openerp import models, api, fields, _

class QualityAlert(models.Model):
    _inherit = "quality.alert"

    #name = fields.Char('Name', index=True, required=True)
    interpod_related_iso_clause = fields.Char("Related ISO Clause", required = False, translate = False)
    interpod_product_category = fields.Many2one("product.category", "Product Category")
    interpod_quality_alert_product_category = fields.Many2one('product.category' , string = "Stage",required = False,  translate = False)
    interpod_ncr_title = fields.Char('Title', required = False, translate = False)
    interpod_linked_documents = fields.Char('Linked Documents', required = False, translate = False)
    interpod_date_ncr_raised = fields.Date('Date Raised', required = False , translate = False)
    interpod_date_ncr_created = fields.Date('Date Created', required = False , translate = False)
    
