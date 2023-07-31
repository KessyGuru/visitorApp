from marshmallow import Schema, fields



class ContactSchema(Schema):
    id = fields.Str(dump_only=True)
    phone_number = fields.Str(required=True)
    email = fields.Str()
    postcode = fields.Str()
    pob = fields.Str()
    physical_address = fields.Str()
    ocupation = fields.Str()
    job_title = fields.Str()
    id_type = fields.Str(required=True)
    id_no = fields.Str(required=True)


class VisitorSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str()
    surname = fields.Str(required=True)

    # contact details
    phone_number = fields.Str(required=True)
    email = fields.Str()
    postcode = fields.Str()
    pob = fields.Str()
    physical_address = fields.Str()
    ocupation = fields.Str()
    job_title = fields.Str()
    id_type = fields.Str(required=True)
    id_no = fields.Str(required=True)

    # contact_id = fields.Int(load_only=True)

    # contact = fields.Nested(ContactSchema())

class GetVisitorSchema(Schema):
    visitor_id = fields.Str(required=True) 

class EmployeeSchema(Schema):
    # id = fields.Str(fields.Integer, primary_key=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str()
    surname = fields.Str(required=True)

    department = fields.Str()
    job_title = fields.Str(required=True)
    is_active = fields.Str()

    phone_number = fields.Str(required=True)
    ext_number = fields.Str()


class AppointmentSchema(Schema):
    visitor_id = fields.Str(required=True)
    employee_id = fields.Str(required=True)

    title = fields.Str(required=True)
    desc = fields.Str()
    appointment_date = fields.DateTime(required=True)
    location = fields.Str(required=True)


class AttendanceSchema(Schema):
    id = fields.Str(dump_only=True)
    is_appointment = fields.Boolean()
    time_out = fields.DateTime()

    # relation ship to -> visitor, emloyee, appointment
    visitor_id = fields.Int(required=True,load_only=True)
    visitor = fields.Nested(VisitorSchema(), dump_only=True)

    employee_id = fields.Int(required=True, load_only=True)
    employee = fields.Nested(EmployeeSchema(), dump_only=True)


