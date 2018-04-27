# -*- coding: utf-8 -*-
{
    'name': "interpod_mail_debranding",

    'summary': """
        Debranding of mail_templates        
    """,

    'description': """
        Debranding of mail_templates
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase', 'account', 'sale'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
