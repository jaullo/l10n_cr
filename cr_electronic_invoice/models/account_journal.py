# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class AccountJournalInherit(models.Model):
    _name = 'account.journal'
    _inherit = 'account.journal'

    sucursal = fields.Integer(string="Branch", required=False, default="1")
    terminal = fields.Integer(string="Terminal", required=False, default="1")
    sequence_electronic_doc_confirmation = fields.Many2one(comodel_name="ir.sequence",
                                                           string="Secuencia de Confirmación de Aceptación "
                                                                  "Comprobante Electrónico",
                                                           required=False)

    sequence_electronic_doc_partial_confirmation = fields.Many2one(comodel_name="ir.sequence",
                                                                   string="Secuencia de Confirmación de"
                                                                          " Aceptación Parcial Comprobante Electrónico",
                                                                   required=False)

    sequence_electronic_doc_reject = fields.Many2one(comodel_name="ir.sequence",
                                                     string="Secuencia de Rechazo Comprobante Electrónico",
                                                     required=False)


    #FE_sequence_id = fields.Many2one("ir.sequence",
    #                                 string="Secuencia de Facturas Electrónicas",
    #                                 required=False)

    #TE_sequence_id = fields.Many2one("ir.sequence",
    #                                 string="Secuencia de Tiquetes Electrónicos",
    #                                 required=False)

    #FEE_sequence_id = fields.Many2one("ir.sequence",
    #                                  string="Secuencia de Facturas Electrónicas de Exportación",
    #                                  required=False)

    #NC_sequence_id = fields.Many2one("ir.sequence",
    #                                 string="Secuencia de Notas de Crédito Electrónicas",
    #                                 required=False)

    #ND_sequence_id = fields.Many2one("ir.sequence",
    #                                 string="Secuencia de Notas de Débito Electrónicas",
    #                                 required=False)

