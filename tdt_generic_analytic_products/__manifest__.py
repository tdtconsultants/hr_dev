# -*- coding: utf-8 -*-
{
    'name': "tdt_generic_analytic_products",

    'summary': """
        Create analytic lines when generic consumable products are consumed in MOs""",

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/manufacturing_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
