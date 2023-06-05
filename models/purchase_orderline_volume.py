from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_weight = fields.Float(compute='_compute_weight', string='Peso total')
    
    @api.depends('order_line')
    def _compute_weight(self):
        for po in self:
            po.total_weight = sum(po.order_line.mapped('total_weight'))
            

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    weight = fields.Float(related='product_id.weight', string='Peso (KG)')
    total_weight = fields.Float(compute='_compute_weight', string='Peso total (KG)')

    @api.depends('product_qty')
    def _compute_weight(self):
        for record in self:
            record.total_weight = record.weight * record.product_qty

