# -*- coding: utf-8 -*-
{
    'name': "tdt_mrp_production_autocomplete",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
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
