import functools

from flask.views import MethodView

from sqlalchemy.exc import SQLAlchemyError

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from db import db
from models import VisitorModel
from forms import CreateVisitorForm

blp = Blueprint('visitorView', __name__, url_prefix='/visitors/')

@blp.route('create/', methods=('GET', 'POST'))
def registerVisitor():
    
    obj_form = CreateVisitorForm()

    if request.method == 'GET':
        return render_template('main/create_visitor.html', form=obj_form)
    elif request.method == 'POST':
        if obj_form.validate_on_submit():
            # first serizile it to the visitor model
            data = obj_form.data
            data.pop('csrf_token')
            obj_form.data.pop('csrf_token')
            obj_seriliazed = VisitorModel(**data)
            try:
                db.session.add(obj_seriliazed)
                db.session.commit()
            except SQLAlchemyError as e:
                return render_template('main/create_visitor.html', error=e)
            
            return redirect('/visitors/list') # send to list of visitors
        else:
            return render_template('main/create_visitor.html', form=obj_form)

@blp.route('list/', methods=('GET',))
def viewVisitors():
    visitors = VisitorModel.query.all()
    return render_template('main/visitors_list.html', visitors=visitors)
