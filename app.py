import os
from flask import Flask, jsonify, render_template
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


from db import db
import models

from resources.visitors import blp as VisitorBlueprint
from resources.attendances import blp as AttendanceBlueprint
from resources.employee import blp as EmployeeBlueprint
from resources.appointments import blp as AppointmentBlueprint
from resources.preview import blp as PreviewBlueprint

def create_app(db_url=None):

    app = Flask(__name__)
    
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Visitor Ledger App"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]= db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.register_blueprint(PreviewBlueprint)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # with app.app_context():
    #     db.create_all()

    api.register_blueprint(VisitorBlueprint)
    api.register_blueprint(AttendanceBlueprint)
    api.register_blueprint(EmployeeBlueprint)
    api.register_blueprint(AppointmentBlueprint)
    return app

app = create_app()


@app.route("/preview")
def get():
    return render_template("base.html")