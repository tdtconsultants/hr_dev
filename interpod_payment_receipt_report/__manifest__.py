# -*- coding: utf-8 -*-
{
    'name': "interpod_payment_receipt_report",

    'summary': """
        Payment Recepit Report
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
    'depends': ['web_enterprise', 'account'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    'demo': [
    ],
    'license': 'OPL-1',
}
