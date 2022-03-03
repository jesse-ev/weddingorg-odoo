from odoo import api, fields, models


class MakanMinum(models.Model):
    _name = 'wedding.makan_minum'
    _description = 'Makanan dan minuman untuk pernikahan'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga (per pax)')
    deskripsi = fields.Text(string='Deskripsi')
    jenis = fields.Selection(string='Makanan/Minuman?', selection=[('makanan', 'Makanan'), ('minuman', 'Minuman'),])
        
