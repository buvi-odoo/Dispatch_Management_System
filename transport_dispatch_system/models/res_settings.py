from odoo import fields, models, api

class resSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
 
    
    module_stock_transport = fields.Boolean(string="Dispatch Management System",store='True')


