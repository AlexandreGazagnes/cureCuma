import datetime
import secrets

from flask import (
    Flask,
    escape,
    request,
    flash,
    url_for,
    render_template,
    Response,
    abort,
    redirect,
    jsonify,
    session,
)

from flask import Blueprint

# from app.forms import InitForm, RunForm
# from app.utils import manage_session
from src import logger

from src.user.forms import CreateUserForm
from src.location.forms import CreateLocationForm


# Blue prints
register = Blueprint("register", __name__)


# static files
@register.route("/register_00", methods=['GET', 'POST'])
def register_00():
    """register 0"""

    logger.debug("called")

    form = CreateUserForm(request.form)
    if request.method == 'POST' :
        logger.critical(form)
        # create user
        # login the user
        # record for user register avancement

        return redirect(url_for('register.register_01'))

    return render_template("pages/register/register_00.html", form=form)



@register.route("/register_01", methods=["GET"])
def register_01():
    """register 1"""

    logger.debug("called")
    return render_template("pages/register/register_01.html")

@register.route("/register_02", methods=["GET", "POST"])
def register_02():
    """register 2"""

    logger.debug("called")

    form = CreateLocationForm(request.form)
    if request.method == 'POST' :

        # enhance form
        form.created.data = str(datetime.datetime.now())[:19] 
        form.name.data = "chez moi"
        form.user_id.data = "122"
        form.category.data = "construction"
        # create proper dict
        form_dict = {k: getattr(form, k).data for k, v in form._fields.items() if (k not in ["submit", "csrf_token"])}
        # make json
        payload = jsonify(form_dict)
        # make api call

        return redirect(url_for('register.register_03'))

    return render_template("pages/register/register_02.html", form=form)


@register.route("/register_03", methods=["GET"])
def register_03():
    """register 3"""

    logger.debug("called")
    return "hello"