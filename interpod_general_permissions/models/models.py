# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        env = self.env
        group_id = self.env.ref('interpod_general_permissions.interpod_managing_group').id
        if group_id in self.env.user.groups_id.ids:
            return super(SaleOrder, self).action_confirm()
        raise AccessError("Sorry, you are not allowed to confirm a sale order")

    def action_cancel(self):
        env = self.env
        group_id = self.env.ref('interpod_general_permissions.interpod_managing_group').id
        if group_id in self.env.user.groups_id.ids or (self.create_uid == self.env.user_id and self.state == 'draft'):
            return super(SaleOrder, self).action_cancel()
        raise AccessError("Sorry, you are not allowed to cancel this sale order")
