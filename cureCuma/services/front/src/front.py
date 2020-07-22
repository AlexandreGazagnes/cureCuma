# import secrets

# from flask import (
#     Flask,
#     escape,
#     request,
#     flash,
#     url_for,
#     render_template,
#     Response,
#     abort,
#     redirect,
#     jsonify,
#     session,
# )

# from flask import Blueprint

# # from app.forms import InitForm, RunForm
# # from app.utils import manage_session
# from src import logger

# # Blue prints
# front = Blueprint("front", __name__)


# # static files
# @front.route("/", methods=["GET"])
# def just_static():
#     """just return html and css"""

#     logger.debug("called")
#     return render_template("pages/home.html")
