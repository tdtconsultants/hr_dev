from openerp import models, api, fields, _

class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    #name = fields.Char('Name', index=True, required=True)
    interpod_asset_number = fields.Char("Planned Payment Date", required = False, translate = False)

