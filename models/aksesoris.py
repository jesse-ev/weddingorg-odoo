from odoo import api, fields, models


class Aksesoris(models.Model):
    _name = 'wedding.aksesoris'
    _description = 'Aksesoris'

    name = fields.Char(string='Nama')
    harga = fields.Integer(string='Harga')
    sponsor = fields.Boolean(string='Sponsor?')


    
    
