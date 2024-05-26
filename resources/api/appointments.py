from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AppointmentModel
from schemas import AppointmentSchemaCreate, AppointmentSchemaUpdate


blp = Blueprint("appointment", __name__, "Operations on appointments")



@blp.route("/appointments/")
class Appointment(MethodView):

    @blp.arguments(AppointmentSchemaCreate)
    @blp.response(200, AppointmentSchemaCreate)
    def post(self, appointment_data): 
           
        print("Appointment Data->", appointment_data)
        appointment = AppointmentModel(**appointment_data)
        try:
            db.session.add(appointment)
            db.session.commit()
        except SQLAlchemyError as e:
            sql_error_message  = str(e.orig)
            print(sql_error_message)
            abort (400, f"{sql_error_message}")
     
@blp.route("/visitor/<int:visitor_id>/appointments/")
class GetVisitorAppointment(MethodView):
    
    @blp.response(200, AppointmentSchemaCreate(many=True))
    def get(self, visitor_id):
        appointments = AppointmentModel.query.filter_by(visitor_id=int(visitor_id)).all()
        
        return appointments

@blp.route("/employee/<int:employee_id>/appointments/")
class GetEmployeeAppointment(MethodView):
    
    @blp.response(200, AppointmentSchemaCreate(many=True))
    def get(self, employee_id):
        appointments = AppointmentModel.query.filter_by(employee_id=int(employee_id)).all()
        
        return appointments

@blp.route("/appointments/<int:appointment_id>/")
class UpdateAppointment(MethodView):
    @blp.arguments(AppointmentSchemaUpdate)
    @blp.response(200, AppointmentSchemaUpdate)
    def patch(self, appointment_data, appointment_id):
        # print({**appointment_data})
        appointment_db_data = AppointmentModel.query.get(int(appointment_id))
        if appointment_db_data:
            appointment_db_data = AppointmentModel(**appointment_data)
        else:
            abort(404, f"Appointment not Found!")
        
        try:
            db.session.add(appointment_db_data)
            db.session.commit()
        except SQLAlchemyError as e:
            sql_error_message  = str(e.orig)
            print(sql_error_message)
            abort (400, f"{sql_error_message}")
        
        return appointment_db_data
    
