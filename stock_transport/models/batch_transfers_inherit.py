from odoo import models, fields,api

class batchTransfers(models.Model):
    _inherit = 'stock.picking.batch'
    fleet_vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicles')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category', string='Category')
    
    weight=fields.Float()
    volume=fields.Float()

    dock_id=fields.Many2one('fleet.dock')

    
    

    
    
    
 