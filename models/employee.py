from odoo import fields,models,api,_

class InheritEmployee(models.Model):
    _inherit = 'hr.employee'

    related_joinee = fields.Many2one('employee.joining.form', string="Related Joinee")
