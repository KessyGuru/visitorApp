from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=True)
    surname = db.Column(db.String(255), nullable=False)

    department = db.Column(db.String(255), nullable=False)
    job_title = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    phone_number = db.Column(db.String(20), nullable=False)
    ext_number = db.Column(db.String(20), nullable=True)

    # relation ship with appointment
    appointment = db.relationship("AppointmentModel", back_populates="employee")

