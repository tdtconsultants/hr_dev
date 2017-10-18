from openerp import models, api, fields, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    #name = fields.Char('Name', index=True, required=True)
    interpod_planned_payment_date = fields.Date("Planned Payment Date", required = False, translate = False)
    interpod_exported = fields.Boolean('Order in sho', required = False, translate=False)

