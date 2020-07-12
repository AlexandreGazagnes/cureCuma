import requests
import time
import json
import datetime
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
from src.routes.response_manager import response_manager
from src.functs.machines.get import machines_get
from src.functs.machines.post import machines_post

machines = Blueprint("machines", __name__)


@machines.route("/machines/ping", methods=["POST", "GET"])
def ping():
    """just a ping for  test"""
    logger.debug("called")

    return response_manager(200, "-", ["pong",], "just a test route")


@machines.route("/machines", methods=["POST", "GET", "PUT", "DELETE"])
def machines_api():
    """just an api"""
    logger.debug("called")

    # get
    if request.method == "GET":
        return machines_get()

    if request.method == "POST":

        logger.critical(request.args)
        logger.critical(request.json)
        logger.critical(request.get_json(force=True))
        return machines_post(request)

    return response_manager(505, "", "", "", "route not handled")
