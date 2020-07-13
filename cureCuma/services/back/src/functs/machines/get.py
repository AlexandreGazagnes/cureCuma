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


def machines_get():
    # gather all / querry all
    try:
        sess = Session()
        payload = sess.query(Machine).all()
        sess.close()
    except Exception as e:
        response_manager(500, "GET", "", e, "fail to query Machine table")
    # payload Transfo
    try:
        if len(payload):
            payload = [i.as_dict() for i in payload]
    except Exception as e:
        response_manager(500, "GET", "", e, "fail to prepare payload")
    # response oK
    return response_manager(200, "GET", payload, mt={"count": len(payload)})

