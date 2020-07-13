from src import logger
from flask import jsonify


def response_manager(s, m, d="", e="", c="", mt={}):
    """return formated response  """

    stxt = "error" if s > 299 else "ok"

    response = {
        "status": stxt,
        "data": d,
        "method": m.lower(),
        "error": e,
        "context": c,
        "meta": mt,
    }
    response = jsonify(response)
    response.status_code = s

    return response

