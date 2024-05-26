from flask.views import MethodView

from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AttendanceModel, EmployeeModel, VisitorModel

from schemas import AttendanceSchema


blp = Blueprint("attendance", __name__, "Attendance operations")

@blp.route("/attendance/")
class AttendanceView(MethodView):

    @blp.response(200, AttendanceSchema(many=True))
    def get(self):
        attendance = AttendanceModel.query.all()
        return attendance
    
    @blp.arguments(AttendanceSchema)
    @blp.response(200, AttendanceSchema)
    def post(self, attended_data):
        attendance = AttendanceModel(**attended_data)
        try:
            db.session.add(attendance)
            db.session.commit()
        except SQLAlchemyError:
            abort(400, "Bad data!")
        
        return attendance
    

