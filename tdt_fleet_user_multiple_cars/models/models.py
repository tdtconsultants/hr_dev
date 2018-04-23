# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    _sql_constraints = [
        ('driver_id_unique', 'Check(1=1)', 'Only one car can be assigned to the same employee!')
    ]


