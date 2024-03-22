from odoo import models, fields,api

class batchTransfers(models.Model):
    _inherit = 'stock.picking.batch'
    fleet_vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicles')
    fleet_category_id = fields.Many2one('fleet.vehicle.model.category', string='Category')
    dock_id=fields.Many2one('fleet.dock')
    total_weight = fields.Float(string='Weight',store="True", compute='_compute_total_weight')
    total_volume = fields.Float( string='Volume',store="True",compute='_compute_total_volume')
    total_weight_ratio=fields.Float(compute='_compute_total_weight',store="True")
    total_volume_ratio=fields.Float(compute='_compute_total_volume', store="True")
    transfer = fields.Float("#Transfer", compute="compute_transfer", store=True)
    move_lines = fields.Float("#Lines", compute="compute_lines", store=True)
    driver_image=fields.Image(related='fleet_vehicle_id.driver_id.image_1920')
    @api.depends("picking_ids")
    def compute_transfer(self):
        for record in self:
            lines = len(record.picking_ids)
            record.transfer = lines
            print(record.transfer)

           

    @api.depends("move_line_ids")
    def compute_lines(self):
        for record in self:
            lines = len(record.move_line_ids)
            print(record.transfer)
            record.move_lines = lines
           

    
    @api.depends('picking_ids.weight')
    def _compute_total_weight(self):
        for batch in self:
            total_weight = 0
            for picking in batch.picking_ids:
                total_weight += picking.weight   
            if(batch.fleet_category_id.max_weight!=0): 
                batch.total_weight_ratio = (total_weight / batch.fleet_category_id.max_weight) * 100 
                batch.total_weight=total_weight 
            else:
                batch.total_weight_ratio=total_weight
                batch.total_weight=total_weight 
            
            
            
    @api.depends('picking_ids.volume')
    def _compute_total_volume(self):
        for batch in self:
            total_volume = 0
            for picking in batch.picking_ids:
                total_volume += picking.volume 
            if(batch.fleet_category_id.max_volume!=0): 
                batch.total_volume_ratio = (total_volume / batch.fleet_category_id.max_volume) * 100 
                batch.total_volume=total_volume
            else:
                batch.total_volume_ratio=total_volume
                batch.total_volume=total_volume 


    # @api.depends('total_weight', 'total_volume')
    # def _compute_display_name(self):
    #     for batch in self:
    #         batch.display_name = f"{batch.fleet_vehicle_id.location}: {batch.total_weight}kg, {batch.total_volume}m\N{SUPERSCRIPT THREE} {batch.fleet_vehicle_id.driver_id.name}"