# -*- coding: utf-8 -*-
{
    'name': "interpod_quality_survey",

    'summary': """
        Enables the creation of surveys to make quality checks on the completion of manufacturing orders""",

    'description': """
    """,

    'author': "TDT Consultants",
    'website': "http://www.tdtconsultants.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'tdt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['quality_mrp','survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/manufacturing_order.xml',
        'views/product_template.xml',
        'views/survey_templates.xml',
        'data/quality_point_test_type.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'OPL-1',
}
