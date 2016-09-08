# -*- coding: utf-8 -*-
from openerp import http

# class Https-connectivity(http.Controller):
#     @http.route('/https-connectivity/https-connectivity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/https-connectivity/https-connectivity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('https-connectivity.listing', {
#             'root': '/https-connectivity/https-connectivity',
#             'objects': http.request.env['https-connectivity.https-connectivity'].search([]),
#         })

#     @http.route('/https-connectivity/https-connectivity/objects/<model("https-connectivity.https-connectivity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('https-connectivity.object', {
#             'object': obj
#         })