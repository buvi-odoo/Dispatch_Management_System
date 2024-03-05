from odoo import fields, models, api

class resSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
    
    module_transport_management = fields.Boolean(String="Dispatch Management System")
    @api.onchange('module_transport_management')
    def set_values(self):
        super(resSettings, self).set_values()
        
        if self.module_transport_management:
            self.env['ir.module.module'].sudo().search([('name', '=', 'stock_transport')]).button_immediate_install()
            self.module_transport_management = True