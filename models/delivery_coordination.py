# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DeliveryCoordination(models.Model):
    _name = 'delivery.coordination'
    _description = 'Delivery Coordination'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'delivery_date desc, id desc'

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default='New')
    
    # Fechas
    request_date = fields.Date(
        string='Fecha de Solicitud', 
        required=True,
        help='Fecha en que llegó la coordinación'
    )
    date = fields.Date(
        string='Fecha de Registro', 
        default=fields.Date.today, 
        required=True,
        readonly=True,
        help='Fecha en que se creó este registro'
    )
    delivery_date = fields.Date(
        string='Fecha de Entrega', 
        required=True,
        help='Fecha programada para la entrega'
    )
    
    # Cliente
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    
    # Contacto de entrega
    delivery_contact_id = fields.Many2one('res.partner', string='Contacto de Entrega')
    delivery_contact_phone = fields.Char(string='Teléfono de Contacto', related='delivery_contact_id.phone', readonly=False)
    delivery_address = fields.Text(string='Dirección de Entrega')
    
    # Técnicos
    technician_ids = fields.Many2many('res.partner', 'delivery_coordination_technician_rel', 'coordination_id', 'technician_id', string='Técnicos Asignados')
    
    # Vehículos (como etiquetas)
    vehicle_ids = fields.Many2many('delivery.vehicle', string='Vehículos')
    
    # Notas
    notes = fields.Html(string='Notas y Detalles')
    
    # Estado
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('in_transit', 'En Tránsito'),
        ('delivered', 'Entregado'),
    ], string='Estado', default='draft', required=True, tracking=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('delivery.coordination') or 'New'
        return super(DeliveryCoordination, self).create(vals)


class DeliveryVehicle(models.Model):
    _name = 'delivery.vehicle'
    _description = 'Delivery Vehicle'

    name = fields.Char(string='Vehículo', required=True)
    color = fields.Integer(string='Color')