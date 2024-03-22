# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    down_payment_product_id = fields.Many2one(
        "product.product",
        string="Down Payment Product",
        help="This product will be used as down payment on a sale order.",
    )