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

from src.model.tables import engine, Session, Machine

machines = Blueprint("machines", __name__)


@machines.route("/machines/ping", methods=["POST", "GET"])
def ping():
    """just a ping for  test"""
    logger.debug("called")

    return "pong", 200


@machines.route("/machines", methods=["POST", "GET", "PUT", "DELETE"])
def machines_api():
    """just an api"""
    logger.debug("called")

    # get
    if request.method == "GET":
        # gather all
        sess = Session()
        data_payload = sess.query(Machine).all()
        sess.close()
        # payload
        if len(data_payload):
            data_payload = [i.as_dict() for i in data_payload]
        # response
        response = {"status": "ok", "data": data_payload, "method": "GET", "error": ""}
        response = jsonify(response)
        response.status_code = 200
        return response

    # default
    response = {
        "status": "error",
        "data": "",
        "method": "GET",
        "error": "not implemented",
    }
    response = jsonify(response)
    response.status_code = 500
    return response

