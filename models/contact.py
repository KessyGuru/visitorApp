from db import db
from sqlalchemy.sql import func


class ContactModel(db.Model):
    __tablename__ = "contacts"


    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    postcode = db.Column(db.Integer, nullable=True)
    pob = db.Column(db.String(255), nullable=True)
    physical_address = db.Column(db.String(255), nullable=True)
    ocupation = db.Column(db.String(255), nullable=True)
    job_title = db.Column(db.String(255), nullable=True)
    id_type = db.Column(db.String(255), nullable=False)
    id_no = db.Column(db.String(255),nullable=False)


    # related to visitor
    # visitor_id = db.Column(db.Integer, db.ForeignKey("visitors.id", name="fk_contact_visitor"), unique=True)
    # visitor_rel = db.relationship("VisitorModel", backref="contact_address")
