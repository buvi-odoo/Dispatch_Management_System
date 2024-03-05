from odoo import models, fields,api

class batchTransfers(models.Model):
    _inherit = 'stock.picking.batch'
    fleet_vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicles')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category', string='Category')
    
    total_weight = fields.Float(compute='_compute_total_weight', string='Weight')
    total_volume = fields.Float(compute='_compute_total_volume', string='Volume')

    dock_id=fields.Many2one('fleet.dock')
    @api.depends('picking_ids.weight')
    def _compute_total_weight(self):
        for batch in self:
            total_weight = 0
            for picking in batch.picking_ids:
                total_weight += picking.weight   
            if(batch.fleet_category_id.max_weight!=0): 
                batch.total_weight = (total_weight / batch.fleet_category_id.max_weight) * 100  
            else:
                batch.total_weight=total_weight
            
            
            
    @api.depends('picking_ids.volume')
    def _compute_total_volume(self):
        for batch in self:
            total_volume = 0
            for picking in batch.picking_ids:
                total_volume += picking.volume 
            if(batch.fleet_category_id.max_volume!=0): 
                batch.total_volume = (total_volume / batch.fleet_category_id.max_volume) * 100  
            else:
                batch.total_=total_volume