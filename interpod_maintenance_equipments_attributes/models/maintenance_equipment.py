from openerp import models, api, fields, _

class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    #name = fields.Char('Name', index=True, required=True)
    interpod_asset_number = fields.Char("Asset Number", required = False, translate = False)

