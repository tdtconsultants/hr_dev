# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2016 - Almighty Consulting Services. <http://www.almightycs.com>
#
#    @author Almighty Consulting Services <info@almightycs.com>
###########################################################################

{
    'name': 'HR Employee Checklist',
    'version': '1.0',
    'author': 'Almighty Consulting Services',
    'category': 'Human Resources Management',
    'summary': 'Employee Entry and Exit Checklist',
    'description': """Manage Entry and Exit Checklist on Employees
    Entry Checklist
    Employee Checklist
    Employee Entry Checklist
    Employee Exit Checklist
    Hiring Procedure
    Entry Process
    Eployee Data Details
    """,
    'depends': ['hr'],
    'website': 'http://www.almightycs.com',
    'data': [
        "security/ir.model.access.csv",
        "views/employee_view.xml",
    ],
    'images': [
        'static/description/employee_checklist_cover_almightycs.jpg',
    ],
    'application': False,
    'sequence': 1,
    'price': 36,
    'currency': 'EUR',
}
