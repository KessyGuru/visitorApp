from flask import render_template,  Blueprint, request
from flask.views import MethodView


blp = Blueprint("Preview", __name__, "Preview only")

@blp.route("/preview")
class Preview(MethodView):
    def get(self):
        return render_template("base.html")
