from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'
    cabang_tugas = fields.Char(string='Cabang Tempat Bertugas')
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_membership = fields.Boolean(string='Is Membership Package', default=False)
    durasi_hari = fields.Integer(string='Durasi (Hari)')
    fasilitas = fields.Text(string='Fasilitas Membership')


class SaleOrder(models.Model):
    _inherit = 'sale.order'
n    
    jenis_transaksi = fields.Selection([
        ('baru', 'Baru'),
        ('renewal', 'Renewal')
    ], string='Jenis Transaksi', required=True, default='baru', tracking=True)
    
    tanggal_mulai = fields.Date(
        string='Tanggal Mulai Membership', 
        required=True, 
        default=fields.Date.context_today
    )
    
    metode_pembayaran = fields.Selection([
        ('transfer', 'Bank Transfer'),
        ('qris', 'QRIS'),
        ('cc', 'Credit Card'),
        ('cash', 'Cash')
    ], string='Metode Pembayaran')
    
    status_validasi = fields.Selection([
        ('draft', 'Draft'),
        ('to_validate', 'To Validate'),
        ('validated', 'Validated'),
        ('need_revision', 'Need Revision')
    ], string='Status Validasi', default='draft', tracking=True)
    
    catatan_koreksi = fields.Text(
        string='Catatan Koreksi (Dari Admin)', 
        tracking=True,
        help="Diisi oleh Admin Sales jika status diubah menjadi Need Revision"
    )

    def action_submit_validation(self):
        for rec in self:
            rec.status_validasi = 'to_validate'

    def action_validate(self):
        for rec in self:
            rec.status_validasi = 'validated'

    def action_need_revision(self):
        for rec in self:
            rec.message_post(body=f"Transaksi membutuhkan revisi. Catatan: {rec.catatan_koreksi}")
            rec.status_validasi = 'need_revision'
