from odoo import api, fields, models


class Kursi(models.Model):
    _name = 'wedding.kursi'
    _description = 'Kursi buat kawinan (buat pengunjung bukan buat kawin)'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga')
    sponsor = fields.Boolean(string='Sponsor?')
    deskripsi = fields.Char(string='Deskripsi')
    
