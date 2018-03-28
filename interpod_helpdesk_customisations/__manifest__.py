# -*- coding: utf-8 -*-
{
    'name': "interpod_helpdesk_customisations",

    'summary': """
        Make helpdesk visible by all and let the users see only their tickets""",

    'description': """
        
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_enterprise'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
