# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DeliveryCoordination(models.Model):
    _name = 'delivery.coordination'
    _description = 'Delivery Coordination'
    _order = 'date desc, id desc'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string='Date', default=fields.Date.today, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    truck = fields.Char(string='Truck')
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('in_transit', 'En Tránsito'),
        ('delivered', 'Entregado'),
    ], string='Estado', default='draft', required=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('delivery.coordination') or 'New'
        return super(DeliveryCoordination, self).create(vals)