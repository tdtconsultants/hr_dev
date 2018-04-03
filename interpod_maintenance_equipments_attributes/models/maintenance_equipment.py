from openerp import models, api, fields, _

class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    interpod_asset_number = fields.Char("Asset Number", required = False, translate = False)


    @api.one
    def _compute_display_name(self):
        self.display_name = ('[' + self.interpod_asset_number +'] ' + self.name) if self.interpod_asset_number else self.name

    display_name = fields.Char(compute='_compute_display_name')
