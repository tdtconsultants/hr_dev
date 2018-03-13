from odoo import api, fields, models, _

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.multi
    def write(self, values):
        ret = super(MrpWorkorder, self).write(values)
        if 'state' in values and values['state'] == 'done':
            if self.production_id.product_id.autocomplete_manufacturing_order and not self.production_id.workorder_ids.filtered(lambda x: x.state != 'done'):
                try:
                    self.production_id.button_mark_done()
                except:
                    pass

        return ret
