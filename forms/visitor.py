from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired


class CreateVisitorForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    middle_name = StringField('Middle name')
    surname = StringField('surname', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    postcode = StringField('Postcode')
    pob = StringField('P.o.Box')
    physical_address = StringField('Physical Address', validators=[DataRequired()])
    ocupation = StringField('Ocupation', validators=[DataRequired()])
    job_title = StringField('Job title', validators=[DataRequired()])
    id_type = StringField('ID Type', validators=[DataRequired()])
    id_no = StringField('ID No.', validators=[DataRequired()])
