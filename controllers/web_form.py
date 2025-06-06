from odoo.http import request, Controller, route
import base64


class WebFormController(Controller):
    @route(['/joining_form'], auth='public', website=True)
    def joining_web_form(self, **kwargs):
        department = request.env['hr.department'].sudo().search([])
        relation = request.env['hr.employee.relation'].sudo().search([('name', '=', 'Father')])
        relation2 = request.env['hr.employee.relation'].sudo().search([('name', '=', 'Mother')])
        relation3 = request.env['hr.employee.relation'].sudo().search([])
        relation4 = request.env['hr.employee.relation'].sudo().search([])
        relation5 = request.env['hr.employee.relation'].sudo().search([])
        values = {}
        values.update({
            'department': department,
            'relation': relation,
            'relation2': relation2,
            'relation3': relation3,
            'relation4': relation4,
            'relation5': relation5
        })
        return request.render('employee_joining_form.joining_web_form_template', values)

    @route('/joining_form/submit', type='http', csrf=False, auth='public', website=True, methods=['POST'])
    def web_form_submit(self, **kw):
        print(kw, 'details')
        father_photo = kw.get('father_photo')
        mother_photo = kw.get('mother_photo')
        child_photo = kw.get('child_photo')
        child2_photo = kw.get('child2_photo')
        child3_photo = kw.get('child3_photo')

        childes = []
        # childes.append(1)
        # childes.append(2)
        childes.append((0, 0, {
            'name': kw.get('father_name'),
            'dob': kw.get('father_dob'),
            'mobile_number': kw.get('father_number'),
            'relation': kw.get('father_relation'),
            'photo': base64.b64encode(father_photo.read()),

        }))
        childes.append((0, 0, {
            'name': kw.get('mother_name'),
            'dob': kw.get('mother_dob'),
            'mobile_number': kw.get('mother_number'),
            'relation': kw.get('mother_relation'),
            'photo': base64.b64encode(mother_photo.read()),

        }))
        if kw.get('child_dob'):
            childes.append((0, 0, {
                'name': kw.get('child_name'),
                'dob': kw.get('child_dob'),
                'mobile_number': kw.get('child_number'),
                'relation': kw.get('child_relation'),
                'photo': base64.b64encode(child_photo.read()),

            }))
        if kw.get('child2_dob'):
            childes.append((0, 0, {
                'name': kw.get('child2_name'),
                'dob': kw.get('child2_dob'),
                'mobile_number': kw.get('child2_number'),
                'relation': kw.get('child2_relation'),
                'photo': base64.b64encode(child2_photo.read()),

            }))
        if kw.get('child3_dob'):
            childes.append((0, 0, {
                'name': kw.get('child3_name'),
                'dob': kw.get('child3_dob'),
                'mobile_number': kw.get('child3_number'),
                'relation': kw.get('child3_relation'),
                'photo': base64.b64encode(child3_photo.read()),

            }))

        print(childes, 'childes')
        file = kw.get('upload_cv')
        photo = kw.get('upload_phone')
        paan = kw.get('upload_paan')
        aadhar = kw.get('upload_aadhar')
        baank = kw.get('upload_passbook')
        request.env['employee.joining.form'].sudo().create({
            'name': kw.get('employee_name'),
            'designation': kw.get('designation'),
            'mail_id': kw.get('mail_id'),
            'office_phone': kw.get('office_number'),
            'phone_number': kw.get('phone_number'),
            'office_mail': kw.get('office_mail_id'),
            'address': kw.get('address'),
            'date_of_birth': kw.get('birth'),
            'date_of_joining': kw.get('joining'),
            'bank_name': kw.get('bank_name'),
            'branch_bank': kw.get('branch'),
            'bank_acc_number': kw.get('account_number'),
            'ifsc_code': kw.get('ifsc'),
            'micr_code': kw.get('micr'),
            'branch': kw.get('branch'),
            'data_line_ids': childes,
            'aadhar_card_number': kw.get('aadhar_number'),
            'pan_card_number': kw.get('pan_number'),
            'marital_stats': kw.get('marital_stats'),
            'blood_group': kw.get('blood_group'),
            'pf_uan_number': kw.get('pf_number'),
            'esi_ip_number': kw.get('esi_number'),
            # 'spouse_dob': kw.get('spouse_dob'),
            'spouse_name': kw.get('spouse_name'),
            'number_of_childes': kw.get('number_of_children'),
            'upload_cv': base64.b64encode(file.read()),
            'photo': base64.b64encode(photo.read()),
            'aadhar_photo': base64.b64encode(aadhar.read()),
            'pan_photo': base64.b64encode(paan.read()),
            'bank_passbook': base64.b64encode(baank.read()),
            'gender': kw.get('gender'),
            'department_id': kw.get('department'),
            'work_location': kw.get('work_location'),
            'work_place': kw.get('work_place'),
            'highest_education_college_name': kw.get('highest_education_college'),
            'highest_education_full_time_or_partime': kw.get('highest_education_time'),
            'highest_education_degree': kw.get('highest_education_education'),
            'highest_education_qualification_specialization': kw.get('highest_education_specialization'),
            'highest_education_qualification_passed_out_month_year': kw.get('highest_education_year'),
            'previous_employment_company_name': kw.get('previous_employment_company'),
            'previous_employment_company_location': kw.get('previous_employment_company_location'),
            'previous_employment_company_designation': kw.get('previous_employment_designation'),
            'previous_employment_company_tenure': kw.get('previous_employment_company_tenure'),
            'total_years_of_experience': kw.get('total_years_of_experience'),
            'emergency_contact_person_name': kw.get('emergency_contact_person_name'),
            'emergency_contact_person_relationship': kw.get('emergency_contact_person_relationship'),
            'emergency_contact_person_mobile_number': kw.get('emergency_contact_person_mobile_number'),
            'emergency_contact_person_email': kw.get('emergency_contact_person_mail'),
            'emergency_contact_person_correspondence_address': kw.get(
                'emergency_contact_correspondence_address'),
            'emergency_details_any_allergies_specifically': kw.get('emergency_details_any_allergies'),
            'nominee_name': kw.get('nominee_name'),
            'nominee_relation': kw.get('nominee_relationship'),
            'nominee_id_proof': kw.get('nominee_id_proof'),
            'skills': kw.get('skills'),
            'hobbies': kw.get('hobbies'),
            'certification': kw.get('certification'),


            # 'phone': post.get('phone'),
            # 'email': post.get('email'),
        })
        return request.render("employee_joining_form.tijus_employee_form_success")
