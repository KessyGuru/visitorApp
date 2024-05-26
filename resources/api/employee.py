import uuid
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from flask_smorest import Blueprint, abort


from db import db
from models import EmployeeModel
from schemas import EmployeeSchema, ContactSchema

blp = Blueprint("employee", __name__,"Operations on Employee.")

@blp.route("/employee/create/")
class Employee(MethodView):
    @blp.arguments(EmployeeSchema)
    @blp.response(200, EmployeeSchema)
    def post(self, employee_data):
        # print({**employee_data})
        employee = EmployeeModel(**employee_data)
        try:
            db.session.add(employee)
            db.session.commit()
        except  SQLAlchemyError:
            print(SQLAlchemyError)
            abort(400, "Bad data!")
        return employee
    
@blp.route("/employees/")
class GetEmployees(MethodView):
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        employees = EmployeeModel.query.all()
        return employees
