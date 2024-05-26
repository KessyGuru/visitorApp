import uuid
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from flask_smorest import Blueprint, abort


from db import db
from models import VisitorModel, ContactModel
from schemas import VisitorSchema, ContactSchema, GetVisitorSchema

blp = Blueprint("visitors", __name__,"Operations on Visitor.")

@blp.route("/visitor/")
class Visitor(MethodView):
    @blp.response(200, VisitorSchema(many=True))
    def get(self):
        visitor = VisitorModel.query.all()
        return visitor


    @blp.response(200, VisitorSchema)
    @blp.arguments(VisitorSchema)
    def post(self, visitor_data):
        # check if visitor is present
        print(visitor_data["phone_number"])
        is_visitor = VisitorModel.query.filter_by(phone_number=visitor_data["phone_number"]).first()
        if is_visitor:
            abort(400,
                  message = 
                    f'Visitor {visitor_data["first_name"]} {visitor_data["surname"]} of phone number: {visitor_data["phone_number"]} exists!'
                    )
        visitor = VisitorModel(**visitor_data)

        try:
            db.session.add(visitor)
            db.session.commit()
        except  SQLAlchemyError:
            abort(400, "Bad data!")
        
        
        return visitor
    
    @blp.arguments(GetVisitorSchema)
    @blp.response(200, VisitorSchema)
    def get(self, visitor_data):
        # print(visitor_data)
        id = visitor_data["visitor_id"]
        visitor = VisitorModel.query.get(int(id))
        return visitor
