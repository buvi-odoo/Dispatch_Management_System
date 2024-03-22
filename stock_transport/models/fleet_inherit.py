from odoo import models, fields,api

class fleetCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'
    max_weight=fields.Integer()
    max_volume=fields.Integer()


    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + f" ({record.max_weight}kg, {record.max_volume}㎥)"
