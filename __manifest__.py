# -*- coding: utf-8 -*-
{
    'name': "Delivery Coordination",
    'summary': "Gestión básica de entregas",
    'description': "Módulo simple para coordinar entregas",
    'author': "Base64Dominicana",
    'category': 'Operations',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/delivery_sequence.xml',
        'views/delivery_coordination_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}