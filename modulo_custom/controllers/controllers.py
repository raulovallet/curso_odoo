from odoo import http
from odoo.http import request


class ModuloCustom(http.Controller):
    @http.route('/modulo_custom/modulo_custom', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/modulo_custom/modulo_custom/objects', auth='public')
    def list(self, **kw):
        return request.render('modulo_custom.listing', {
            'root': '/modulo_custom/modulo_custom',
            'objects': request.env['modulo_custom.modulo_custom'].search([]),
        })

    @http.route('/modulo_custom/modulo_custom/objects/<model("modulo_custom.modulo_custom"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('modulo_custom.object', {
            'object': obj
        })
