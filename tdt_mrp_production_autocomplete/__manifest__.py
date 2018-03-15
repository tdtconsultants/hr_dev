# -*- coding: utf-8 -*-
{
    'name': "tdt_mrp_production_autocomplete",

    'summary': """
        Make a manufacturing order set to done automatically when all its work orders are completed.
        """,

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product.xml',
    ],
}
