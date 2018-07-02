# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    tyre_size = fields.Float(
        string='Tyre Size',
        help='Tyre Size in inches',
    )
