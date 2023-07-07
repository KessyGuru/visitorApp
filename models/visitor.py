from db import db
from sqlalchemy.sql import func


class VisitorModel(db.Model):
    __tablename__ = "visitors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=True)
    surname = db.Column(db.String(255), nullable=False)

    # address and contact infos to be on other table but related here
    contact_address= db.relationship("ContactModel", uselist=False, backref="visitor")

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # other relations
    # appointment 
    appointments = db.relationship("AppointmentModel", back_populates="visitor", lazy="dynamic")

    # attendance
    attendance = db.relationship("AttendanceModel", back_populates="visitor", lazy="dynamic")


