# -*- coding: utf-8 -*-
{
    'name': "tdt_fleet_user_multiple_cars",

    'summary': """
	Allow user to drive multiple cars
    """,

    'description': """
	Allow user to drive multiple cars
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'fleet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['fleet','interpod_hr_employees_customisations'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    'license': 'OPL-1',
}
