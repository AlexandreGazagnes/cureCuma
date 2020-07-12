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


def machines_post(request):

    # gather all
    payload = request.json

    logger.info(payload)
    # no payload
    if not payload:
        return response_manager(500, "POST", "None", "", "not payload")
    # paylod in Obj
    try:
        payload.update(created=str(datetime.datetime.now())[:19])
        machine = Machine(**payload)
    except Exception as e:
        return response_manager(
            500, "POST", payload, e, "error when init Machine Object"
        )

    # add object in db
    try:
        sess = Session()

        sess.add(machine)
        sess.commit()
        sess.close()
        return response_manager(201, "POST", "payload", "", "object created in db")
    except Exception as e:
        try:
            sess.rollback()
        except Exception as e:
            pass
        try:
            sess.close()
        except Exception as e:
            pass
        return response_manager(
            500, "POST", payload, e, "error when init Machine Object"
        )

