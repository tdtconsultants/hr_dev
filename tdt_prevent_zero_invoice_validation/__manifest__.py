# -*- coding: utf-8 -*-
{
    'name': "tdt_prevent_cero_invoice_validation",

    'summary': """
        This module will prevent invoices with Total amount $0 to be validated.
        """,

    'description': """
        This module will prevent invoices with Total amount $0 to be validated.
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
    ],
    'license': 'OPL-1',
}
