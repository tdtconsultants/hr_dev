# -*- coding: utf-8 -*-
{
    'name': "tdt_project_manager_financials",

    'summary': """
        Allow Project Manager to have access to specified accounts.
        """,

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/account.xml',
    ],
}
