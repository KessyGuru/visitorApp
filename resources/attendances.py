import functools

from flask.views import MethodView

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_

from datetime import datetime

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from db import db
from models import VisitorModel, AttendanceModel
from forms import CreateVisitorForm

blp = Blueprint('attendanceView', __name__, url_prefix='/attendance/')

@blp.route('check-in/<int:visitor_id>/', methods=('GET', 'POST',))
def checkInVisitor(visitor_id):
    visitor = VisitorModel.query.get(visitor_id)
    if visitor:
        obj_attendance = AttendanceModel()
        obj_attendance.visitor_id = visitor_id
        obj_attendance.time_in = datetime.utcnow()

        try:
            db.session.add(obj_attendance)
            db.session.commit()
        except SQLAlchemyError as e:
            return render_template('main/attendance_checkin.html', error=e)
        
        return redirect('/attendance/check-in/list/') # send to list of visitors
    else:
        return redirect('/visitors/create',message={
            "message": "Visitor not found, please register!"
        })
    
@blp.route('check-out/<int:visitor_id>/', methods=('GET', 'POST',))
def checkOutVisitor(visitor_id):
    attendance = AttendanceModel.query.filter(and_(AttendanceModel.visitor_id == visitor_id, AttendanceModel.time_out==None)).first()
    if attendance:
        attendance.time_out = datetime.utcnow()
        try:
            db.session.add(attendance)
            db.session.commit()
        except SQLAlchemyError as e:
            return render_template('main/attendance_checkin.html', error=e)
        
        return redirect('/attendance/check-in/list/') # send to list of visitors
    else:
        return redirect('/visitors/create',message={
            "message": "Visitor not found, please register!"
        })
        
@blp.route('check-in/list/', methods=('GET',))
def viewCheckInList():
    attendance = AttendanceModel.query.all()
    return render_template('main/checkin_list.html', attendances=attendance)

