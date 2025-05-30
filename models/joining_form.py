from odoo import fields, models, api, _
from odoo.exceptions import UserError


class EmployeeJoiningForm(models.Model):
    _name = 'employee.joining.form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'Joining Form'

    name = fields.Char(string="Name")
    bank_name = fields.Char(string='Bank Name')
    spouse_name = fields.Char(string='Spouse Name')
    name_of_children = fields.Text(string='Name Of Childrens')
    bank_acc_number = fields.Char(string='Account Number')
    branch_bank = fields.Char(string='Branch')
    ifsc_code = fields.Char(string='IFSC Code')
    micr_code = fields.Char(string='MICR Code')
    aadhar_card_number = fields.Char(string='Aadhar Card Number')
    pan_card_number = fields.Char(string='Pan Card Number')
    pf_uan_number = fields.Char(string='PF UAN Number')
    esi_ip_number = fields.Char(string='ESI IP Number')
    blood_group = fields.Char(string='Blood Group')
    employee_name = fields.Char(string='Employee Name')
    designation = fields.Char(string='Designation')
    date_of_joining = fields.Date(string='Date Of Joining')
    date_of_birth = fields.Date(string='Date Of Birth')
    mail_id = fields.Char(string='Personal Email')
    phone_number = fields.Char(string='Personal Phone Number')
    office_phone = fields.Char(string='Office Phone Number')
    office_mail = fields.Char(string='Office Email')
    # spouse_dob = fields.Date(string='Spouse Date Of Birth')
    number_of_childes = fields.Char(string='Number Of Childes')
    marital_stats = fields.Selection([('married', 'Married'), ('single', 'Unmarried')], string='Marital Status')
    address = fields.Text(string='Address')
    fath_rel = fields.Char(string='Father Relation')
    moth_rel = fields.Char(string='Mother Relation')
    state = fields.Selection(selection=[
        ('draft', 'Hr Confirmation'),
        ('confirm', 'IT Confirmation'),
        ('hr_approval', 'HR Approval'),
        ('done', 'Done'), ('archived', 'Archived'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')
    upload_cv = fields.Binary(string='Upload CV')
    aadhar_photo = fields.Binary(string='Aadhar Card Photo')
    pan_photo = fields.Binary(string='Pan Card Photo')
    bank_passbook = fields.Binary(string='Bank Passbook')
    photo = fields.Binary(string='Photo')
    father_number = fields.Char(string='Father Number')
    mother_number = fields.Char(string='Mother Number')
    branch = fields.Char(string='Branch')
    department_id = fields.Many2one('hr.department', string='Department')
    work_location = fields.Char(string='Work Location(city)')
    work_place = fields.Char(string='Work Place(office)')
    highest_education_college_name = fields.Char(string='Highest Education College Name')
    highest_education_full_time_or_partime = fields.Char(
        string='Highest Education Qualification - Full Time / Part Time / Distance Education')
    highest_education_degree = fields.Char(string='Highest Education Qualification - Degree')
    highest_education_qualification_specialization = fields.Char(
        string='Highest Education Qualification - Specialization')
    highest_education_qualification_passed_out_month_year = fields.Char(
        string='Highest Education Qualification - Passed Out Month Year')
    previous_employment_company_name = fields.Char(string='Previous Employment - Company Name')
    previous_employment_company_location = fields.Char(string='Previous Employment - Company Location')
    previous_employment_company_designation = fields.Char(string='Previous Employment - Company Designation')
    previous_employment_company_tenure = fields.Char(string='Previous Employment - Company Tenure')
    total_years_of_experience = fields.Integer(
        string='Total Years Of Experience')
    emergency_contact_person_name = fields.Char(string='Emergency Contact Person Name')
    emergency_contact_person_relationship = fields.Char(string='Emergency Contact Person Relationship')
    emergency_contact_person_mobile_number = fields.Char(string='Emergency Contact Person Mobile Number')
    emergency_contact_person_email = fields.Char(string='Emergency Contact Person Email')
    emergency_contact_person_correspondence_address = fields.Char(
        string='Emergency Contact Person Correspondence Address')
    emergency_details_any_allergies_specifically = fields.Char(string='Emergency Details - Any Allergies Specifically')
    nominee_name = fields.Char(string='Nominee Name')
    nominee_relation = fields.Char(string='Nominee Relation')
    nominee_id_proof = fields.Char(string='Nominee ID Proof Pan or Aadhar')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    skills = fields.Text(string="Skills ")
    hobbies = fields.Text(string="Hobbies and Intersets")
    active_social_media = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                               string='Are you active in social media')
    social_media_urls = fields.Text(string="Social media activities")
    have_you_done_anchoring = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                               string='Have you done anchoring')
    certification = fields.Text(string="Certification")
    insta_url = fields.Char(string="Instagram")
    fb_url = fields.Char(string="Facebook")
    linkedin_url = fields.Char(string="Linkedin")
    related_employee = fields.Many2one('hr.employee', string="Related Employee")

    def action_confirm_employee(self):
        print('hi')
        self.state = 'confirm'

    def action_create_user(self):
        if self.office_mail:
            # Create the user first
            user_vals = {
                'name': self.name,  # User name
                'login': self.office_mail,  # User login (use the office mail or unique field)
                'email': self.office_mail,
                # 'partner_id': 10# User email
            }

            user = self.env['res.users'].create(user_vals)  # Create the user
            print(user.id, 'usr')
            # Call the method to create the employee and link it to this user
            self.action_create_employee(user)
            # Change the state to 'done'
            self.state = 'hr_approval'
        else:
            raise UserError('please add office mail for this employee')

    def action_create_employee(self, user):
        # Create the employee and link it to the user

        employee_vals = {
            'name': self.name,
            'job_title': self.designation,
            'mobile_phone': self.office_phone,
            'work_email': self.office_mail,
            'department_id': self.department_id.id,
            'user_id': user.id,
            'related_joinee': self.id,
            'joining_date': self.date_of_joining,

        }

        # Create the employee
        employee = self.env['hr.employee'].create(employee_vals)
        last_employee = self.env['hr.employee'].sudo().search([], limit=1, order='id desc')
        # Link the user back to the employee (two-way linking)
        # user.partner_id = employee.address_home_id
        self.related_employee = last_employee.id

    def action_cancel(self):
        self.state = 'cancel'

    def action_view_employee(self):
        """ Action to open sale orders related to the partner """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Related Employee',
            'res_model': 'hr.employee',
            'view_mode': 'tree,form',
            'domain': [('related_joinee.id', '=', self.id)],
            'context': "{'create': False}"
        }

    employee_count = fields.Integer(string="Employee", compute="_compute_employee_count")

    def _compute_employee_count(self):
        for partner in self:
            employee = self.env['hr.employee'].search([('related_joinee', '=', partner.id)])
            if employee:
                print(employee.name, 'emp')
                partner.employee_count = self.env['hr.employee'].search_count([('related_joinee', '=', partner.id)])
            else:
                partner.employee_count = 0

    def action_hr_approval(self):
        self.state = 'done'

    def act_archive(self):
        return {'type': 'ir.actions.act_window',
                'name': _('User Archive Clarification'),
                'res_model': 'user.archive.clarification',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.related_employee.user_id.id, 'default_employee_form': self.id}, }
        # if self.related_employee:
        #     print('yess', self.related_employee.user_id.active)
        #     self.related_employee.user_id.active = 0
        #     self.related_employee.active = 0
        #     self.state = 'archived'

    def act_unarchive(self):
        return {'type': 'ir.actions.act_window',
                'name': _('User UnArchive Clarification'),
                'res_model': 'user.unarchive.clarification',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.related_employee.user_id.id, 'default_employee_form': self.id}, }
