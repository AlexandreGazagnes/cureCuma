import requests
import time
import json
from dateutil.parser import parse

from flask import (
    Flask,
    escape,
    request,
    flash,
    url_for,
    render_template,
    abort,
    redirect,
)
from flask import Blueprint
from flask import jsonify

from params import GeneralParams as Params
from src import logger

# from src.model.tables import engine, Session, Sale, Transaction, Membre

users = Blueprint("users", __name__)


@users.route("/users/ping", methods=["POST", "GET"])
def ping():
    """just a ping"""
    logger.debug("called")

    return "pong", 200
