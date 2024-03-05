from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    volume = fields.Float(string='Volume', compute='_compute_weight_volume')
    weight = fields.Float(stirng="Weight", compute='_compute_weight_volume')
    
    
    @api.depends('move_ids.move_line_ids.product_id.weight', 'move_ids.move_line_ids.product_id.volume', 'move_ids')
    def _compute_weight_volume(self):
     for record in self:
        total_weight = 0
        total_volume = 0
        for move in record.move_ids:
            for move_line in move.move_line_ids:
                quantity = move_line.move_id.product_qty
                total_weight += move_line.product_id.weight * quantity
                total_volume += move_line.product_id.volume * quantity
        record.weight = total_weight
        record.volume = total_volume
        print(total_volume)
        print(total_weight)