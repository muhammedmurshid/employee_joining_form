from odoo import fields,models,api,_
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class UserArchiveClarification(models.TransientModel):
    _name = "user.archive.clarification"

    user_id = fields.Many2one('res.users', string="User")
    clarification = fields.Text(default="Are you sure you want to archive this user?", readonly=1)
    sure = fields.Boolean(string=" ")
    employee_form = fields.Many2one('employee.joining.form', string="Employee Form")

    def act_archive(self):
        if self.user_id:
            self.user_id.active = 0
            self.user_id.employee_id.active = 0
            self.employee_form.state = 'archived'
            self.employee_form.resigned_date = datetime.today()
            self.employee_form.archived_on = self.env.user.id
        else:
            raise UserError(
                _("Please Add Related Employee"))


class UserUnArchiveClarification(models.TransientModel):
    _name = "user.unarchive.clarification"

    user_id = fields.Many2one('res.users', string="User")
    clarification = fields.Text(default="Are you sure you want to unarchive this user?", readonly=1)
    sure = fields.Boolean(string=" ")
    employee_form = fields.Many2one('employee.joining.form', string="Employee Form")

    def act_unarchive(self):
        if self.user_id:
            print(self.user_id.employee_id, 'un archive')
            self.user_id.active = 1
            self.user_id.employee_id.active = 1
            self.employee_form.state = 'done'
