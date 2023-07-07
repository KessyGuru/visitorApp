from db import db


class AttendanceModel(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    is_appointment = db.Column(db.Boolean, default=False)
    time_in = db.Column(db.DateTime(timezone=True), nullable=False)
    time_out = db.Column(db.DateTime(timezone=True), nullable=True)

    # relation ship to -> visitor, emloyee, appointment
    visitor_id = db.Column(db.Integer, db.ForeignKey("visitors.id"))
    visitor = db.relationship("VisitorModel", back_populates="attendance")