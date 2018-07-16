# -*- coding: utf-8 -*-
{
    'name': "interpod_hr_employees_customisations",

    'summary': """
        """,

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'hr_contract',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
