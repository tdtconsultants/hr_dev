from openerp import models, api, fields, _

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    #name = fields.Char('Name', index=True, required=True)
    interpod_planned_payment_date = fields.Date("Planned Payment Date", required = False, translate = False)
    interpod_exported = fields.Boolean('Exported', required = False, translate=False)

@api.model
def create(self, vals):
    move_line = super(AccountMoveLine, self.with_context(check_move_validity=False)).create(vals)
    return move_line

@api.multi
def write(self, vals):
    move_line = super(AccountMoveLine, self.with_context(check_move_validity=False)).write(vals)
    return move_line
