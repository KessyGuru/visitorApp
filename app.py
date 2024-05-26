import os
from flask import Flask, jsonify, render_template
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect


from db import db
import models

## View Endpoints
from resources.visitors import blp as VisitorViewBlueprint
from resources.attendances import blp as AttendanceViewBlueprint

## API Endpoints
from resources.api.visitors import blp as VisitorBlueprint
from resources.api.attendances import blp as AttendanceBlueprint
from resources.api.employee import blp as EmployeeBlueprint
from resources.api.appointments import blp as AppointmentBlueprint
from resources.api.preview import blp as PreviewBlueprint



def create_app(db_url=None):

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'abc'
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Visitor Ledger App"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]= db_url or os.getenv("DATABASE_URL", "sqlite:///data_db.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    csrf = CSRFProtect(app)

    ## Normal Endpoints
    # app.register_blueprint(VisitorViewBlueprint)
    # app.register_blueprint(AttendanceViewBlueprint)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # with app.app_context():
    #     db.create_all()

    ## API Endpoints
    api.register_blueprint(VisitorBlueprint)
    api.register_blueprint(AttendanceBlueprint)
    api.register_blueprint(EmployeeBlueprint)
    api.register_blueprint(AppointmentBlueprint)
    return app

app = create_app()


@app.route("/preview")
def get():
    return render_template("main/create_visitor.html")
