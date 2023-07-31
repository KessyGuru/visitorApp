from db import db
from sqlalchemy.sql import func


class VisitorModel(db.Model):
    __tablename__ = "visitors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=True)
    surname = db.Column(db.String(255), nullable=False)

    # address and contact infos to be on other table but related here
    # contact_id = db.Column(db.Integer, db.ForeignKey("contacts.id"),nullable=True)
    # contact_address= db.relationship("ContactModel", uselist=False, backref="visitor")


    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=True)
    postcode = db.Column(db.Integer, nullable=True)
    pob = db.Column(db.String(255), nullable=True)
    physical_address = db.Column(db.String(255), nullable=True)
    ocupation = db.Column(db.String(255), nullable=True)
    job_title = db.Column(db.String(255), nullable=True)
    id_type = db.Column(db.String(255), nullable=False)
    id_no = db.Column(db.String(255),nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # other relations
    # appointment 
    appointments = db.relationship("AppointmentModel", back_populates="visitor", lazy="dynamic")

    # attendance
    attendance = db.relationship("AttendanceModel", back_populates="visitor", lazy="dynamic")




