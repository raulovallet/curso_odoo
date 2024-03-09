from odoo import models, fields, api, _


class ModelName(models.Model):
    _name = 'ModelName'
    _description = 'ModelName'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        string='Name',
        required=True,
        default=lambda self: _('New'),
        copy=False
    )
