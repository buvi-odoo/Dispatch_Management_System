from odoo import models, fields,api

class fleetCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'
    max_weight=fields.Integer()
    max_volume=fields.Integer()


    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.max_weight or record.max_volume:
                name += f" ({record.max_weight}kg, {record.max_volume}㎥)"
            record.display_name = name
