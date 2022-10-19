# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Daily Loading Management',
    'version' : '1.0.0',
    'summary': '',
    'sequence': 10,
    'description': """This module will be regarding Loading management which is being done manually by store team, to make things more accurate andautonomous, we are developing this module.""",
    'category': 'Loading Management',
    'author': 'Asim Jamil',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/daily_loading_list.xml',
    ],
    'demo': [],
    'installable': True,
    'application' : True,
    'auto_install': False,
    'assets': {},
    'license' : 'LGPL-3'
}
