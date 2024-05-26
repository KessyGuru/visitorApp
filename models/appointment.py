from db import db
from sqlalchemy.sql import func

class AppointmentModel(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    appointment_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255),nullable=False)
    appointment_via = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # relationship
    visitor_id = db.Column(db.Integer, db.ForeignKey("visitors.id"))

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"))

