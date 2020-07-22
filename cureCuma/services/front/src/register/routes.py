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

# Blue prints
register = Blueprint("register", __name__)


# static files
@register.route("/register_0", methods=["GET"])
def register_0():
    """register 0"""

    logger.debug("called")
    return "register_0"
