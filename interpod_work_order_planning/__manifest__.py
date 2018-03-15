# -*- coding: utf-8 -*-
{
    'name': "interpod_work_order_planning",

    'summary': """
        Enables the overlapping of workorders""",

    'description': """
        Select which workcenters can work in parallel and the capacity
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp_workorder'],

    # always loaded
    'data': [
        'views/work_center.xml',
        'views/mrp_routing.xml',
        'data/server_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
