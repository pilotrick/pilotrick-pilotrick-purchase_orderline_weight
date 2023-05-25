from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_weight = fields.Float(compute='_compute_weight', string='Total Peso')
    
    @api.depends('order_line')
    def _compute_vol(self):
        for po in self:
            po.total_weight = sum(po.order_line.mapped('total_weight'))
            

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    weight = fields.Float(related='product_id.weight', string='Volumne(KG)')
    total_weight = fields.Float(compute='_compute_weight', string='Total Weight(KG)')

    @api.depends('weight')
    def _compute_volume(self):
        for record in self:
            record.total_weight = record.weight * record.product_qty

