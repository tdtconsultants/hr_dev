# -*- coding: utf-8 -*-
{
    'name': "interpod_general_permissions",

    'summary': """
        Module that contains some of interpods' record rules and access controls""",

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','project'],

    # always loaded
    'data': [
        'data/groups.xml',
        'security/ir.model.access.csv',   
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
