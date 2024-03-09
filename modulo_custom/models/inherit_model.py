from odoo import models, fields, api, _


class ModelName(models.Model):
    _inherit = 'ModelName'

    field_name = fields.Char(
        string='Field Name',
    )
