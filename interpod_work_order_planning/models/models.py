# -*- coding: utf-8 -*-

from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import math
import copy
from odoo import api, fields, models, tools
import logging

_logger = logging.getLogger(__name__)

class MrpWorkCenter(models.Model):
    _inherit = 'mrp.workorder'

    @api.one
    def _compute_interpod_color(self):
        color_codes = { 'pending': 3, ## yellow
                        'progress': 8, ## blue
                        'ready': 10, ## green
                        'cancel': 9, ## green
                        'done': 0 ## white (doesn't appear on kanban)
                      }
        self.interpod_color = color_codes.get(self.state, 6)

    interpod_color = fields.Integer(compute='_compute_interpod_color')


class MrpWorkCenter(models.Model):
    _inherit = 'mrp.workcenter'

    works_in_parallel = fields.Boolean(default=False, help="Select this if you want this work center to allow overlapping work orders")

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def button_plan(self):
        res = super(MrpProduction, self).button_plan()
        WorkOrder = self.env['mrp.workorder']
        ProductUom = self.env['product.uom']
        for order in self.filtered(lambda x: x.state == 'planned'):
            order.workorder_ids.write({'date_planned_start': False, 'date_planned_finished': False})

        # Schedule all work orders (new ones and those already created)
        for order in self:
            start_date = order._get_start_date()
            from_date_set = False
            for workorder in order.workorder_ids:
                workcenter = workorder.workcenter_id
                wos = WorkOrder.search([('workcenter_id', '=', workcenter.id), ('date_planned_finished', '<>', False),
                                        ('state', 'in', ('ready', 'pending', 'progress')),
                                        ('date_planned_finished', '>=', start_date.strftime(tools.DEFAULT_SERVER_DATETIME_FORMAT))], order='date_planned_start')
                from_date = start_date
                calendar = workcenter.resource_calendar_id
                to_date = calendar.plan_hours(workorder.duration_expected / 60.0, from_date)
                if not to_date:
                    if not from_date_set:
                        from_date = intervals[0][0]
                        from_date_set = True
                    to_date = from_date + relativedelta(minutes=workorder.duration_expected)
                original_from_date = from_date
                original_to_date = to_date
                if workcenter.capacity > 1 and workcenter.works_in_parallel:
                    ### work in parallel
                    wo_intervals = []
                    intervals = []
                    for wo in wos:
                        if from_date < fields.Datetime.from_string(wo.date_planned_finished) and (to_date > fields.Datetime.from_string(wo.date_planned_start)):
                            i_from_date = fields.Datetime.from_string(wo.date_planned_start)
                            if i_from_date < from_date:
                                i_from_date = from_date
                            i_to_date = fields.Datetime.from_string(wo.date_planned_finished)
                            if not i_to_date:
                                i_to_date = i_from_date + relativedelta(minutes=workorder.duration_expected)
                            wo_intervals.append({'from_date': i_from_date, 'to_date':i_to_date, 'producing':wo.qty_remaining})
                            if i_from_date not in intervals:
                                intervals.append(i_from_date)
                            if i_to_date not in intervals:
                                intervals.append(i_to_date)
                    duration = workorder.duration_expected### Duration of the workorder
                    if intervals:
                        sorted_intervals = sorted(intervals)  ####copy.deepcopy(wo_intervals)
                        capacities = [workcenter.capacity] * (len(sorted_intervals) - 1) 
                        index = 0
                        for interval_start_date in sorted_intervals:
                            if len(sorted_intervals) == (index + 1):
                                break
                            for j in wo_intervals:
                                interval_finish_date = sorted_intervals[index + 1]
                                if j['from_date'] < interval_finish_date and j['to_date'] > interval_start_date: ### 
                                    capacities[index] -= j['producing']
                            index = index + 1
                        i = 0
                        from_date = None
                        to_date = None
                        while i < len(capacities):
                            if from_date and to_date:
                                break
                            if workorder.qty_production <= capacities[i]:
                                tentative_to_date = workcenter.resource_calendar_id.attendance_ids and workcenter.resource_calendar_id.plan_hours(workorder.duration_expected / 60.0, sorted_intervals[i])
                                #if (sorted_intervals[i+1] - sorted_intervals[i]).total_seconds() >= duration * 60:
                                if tentative_to_date < sorted_intervals[i+1]:
                                    from_date = sorted_intervals[i]
                                    to_date = tentative_to_date
                                    break
                                else:
                                    j = i + 2
                                    if j > (len(capacities) - 1):
                                        ### No more workorders to check, and intervals(i-j) have capacity
                                        from_date = sorted_intervals[i]
                                        to_date = tentative_to_date 
                                    else:
                                        next_interval_cap = capacities[i+1]
                                        while (next_interval_cap >= workorder.qty_production):
                                            if tentative_to_date < sorted_intervals[j]:
                                            #if (sorted_intervals[j] - sorted_intervals[i]).total_seconds() >= duration * 60:
                                                from_date = sorted_intervals[i]
                                                to_date = tentative_to_date 
                                                break
                                            else:
                                                if j > (len(capacities) - 1):
                                                    break
                                                next_interval_cap = capacities[j]
                                                j = j + 1
                                    i = j
                            else:
                                i = i + 1
                        if not to_date or not from_date:
                            from_date = sorted_intervals[len(sorted_intervals) - 1]
                            to_date = workcenter.resource_calendar_id.attendance_ids and workcenter.resource_calendar_id.plan_hours(workorder.duration_expected / 60.0, from_date)
                    else:
                        from_date = original_from_date
                        to_date = original_to_date
                else:
                    for wo in wos:
                        if from_date < fields.Datetime.from_string(wo.date_planned_finished) and (to_date > fields.Datetime.from_string(wo.date_planned_start)):
                            from_date = fields.Datetime.from_string(wo.date_planned_finished)
                            to_date = workcenter.resource_calendar_id.attendance_ids and workcenter.resource_calendar_id.plan_hours(workorder.duration_expected / 60.0, from_date)
                            if not to_date:
                                to_date = from_date + relativedelta(minutes=workorder.duration_expected)
                workorder.write({'date_planned_start': from_date, 'date_planned_finished': to_date})

                if (workorder.operation_id.batch == 'no') or (workorder.operation_id.batch_size >= workorder.qty_production):
                    start_date = to_date
                else:
                    qty = min(workorder.operation_id.batch_size, workorder.qty_production)
                    cycle_number = math.ceil(qty / workorder.production_id.product_qty / workcenter.capacity)
                    duration = workcenter.time_start + cycle_number * workorder.operation_id.time_cycle * 100.0 / workcenter.time_efficiency
                    to_date = workcenter.resource_calendar_id.attendance_ids and workcenter.resource_calendar_id.plan_hours(duration / 60.0, from_date)
                    if not to_date:
                        start_date = from_date + relativedelta(minutes=duration)
        return res


