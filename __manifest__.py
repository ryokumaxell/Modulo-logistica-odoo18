# -*- coding: utf-8 -*-
{
    'name': "Delivery Coordination",
    'summary': "Gestión de entregas logísticas",
    'description': "Módulo para coordinar entregas con técnicos y seguimiento",
    'author': "Tu Empresa",
    'category': 'Operations',
    'version': '18.0.1.0.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/delivery_sequence.xml',
        'views/delivery_coordination_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}