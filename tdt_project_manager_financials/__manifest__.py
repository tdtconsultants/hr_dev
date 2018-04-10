# -*- coding: utf-8 -*-
{
    'name': "tdt_project_manager_financials",

    'summary': """
        Allow Project Manager to have access to specified accounts.
        """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'project','interpod_general_permissions','hr_timesheet','hr_expense','analytic','hr_holidays'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/hide_analytic_accounts.xml',
    ],
    'license': 'OPL-1',
}
