from odoo import api, fields, models
import logging

log = logging.getLogger(__name__)

class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    pelaminan = fields.Many2one(comodel_name='wedding.pelaminan', 
                                string='Tipe Pelaminan', 
                                required=True,
                                )   
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])    
    accesories = fields.Many2one(
        string='Aksesoris',
        comodel_name='wedding.aksesoris',
        required = False,
    )
    jumlah_accesories = fields.Integer(
        string='Jumlah aksesoris',
    )
    kursi = fields.Many2one(
        comodel_name='wedding.kursi', 
        string='Kursi')
    jumlah_kursi = fields.Integer(
        string='Jumlah Kursi',
    )
    makan_minum_id = fields.Many2many(comodel_name='wedding.makan_minum', string='Makanan dan Minuman')
    pax = fields.Integer(string='Jumlah Pax')
    
    

    harga = fields.Char(compute='_compute_harga', string='Harga')
    
    @api.depends('pelaminan', 'jumlah_accesories', 'jumlah_kursi', 'bunga', 'makan_minum_id', 'pax')
    def _compute_harga(self):
        log.debug(self)
        _harga = 0
        for record in self:
            if record.jumlah_accesories < 0:
                record.jumlah_accesories = 0
            if record.jumlah_kursi < 0:
                record.jumlah_kursi = 0
            if record.pax < 0:
                record.pax = 0
            if record.makan_minum_id:
                for makan_minum in record.makan_minum_id:
                    _harga += makan_minum.harga * record.pax
            if record.accesories.sponsor:
                _harga = _harga + (record.accesories.harga + 50000) * record.jumlah_accesories
            else:
                _harga = _harga + record.accesories.harga * record.jumlah_accesories
            if record.kursi.sponsor:
                _harga = _harga + (record.kursi.harga + 50000) * record.jumlah_kursi
            else:
                _harga = _harga + record.kursi.harga * record.jumlah_kursi
            if record.bunga == 'bunga mati':
                _harga = _harga + 75000
            if record.bunga == 'bunga hidup':
                _harga = _harga + 100000
            record.harga = _harga + record.pelaminan.harga
    
    
