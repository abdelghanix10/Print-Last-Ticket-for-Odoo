# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_print_last_receipt = fields.Boolean(
        string='Enable Print Last Receipt Button',
        default=True,
        help='Show button in POS to print the last receipt'
    )
