# -*- coding: utf-8 -*-
{
    'name': "interpod_eco_attributes",

    'summary': """
        ECO views and behavior customizations for Interpod
    """,

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'mrp_plm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/products.xml',
        'views/views.xml',
        'data/checklist.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
    ],
}
