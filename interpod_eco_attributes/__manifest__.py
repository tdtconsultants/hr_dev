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
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'mrp_plm'],

    # always loaded
    'data': [
        'data/products.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
    ],
}
