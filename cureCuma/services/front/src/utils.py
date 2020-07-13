import os
import requests
import datetime
import secrets
import pprint
from pprint import pformat


from flask import session


# import sys
# import subprocess
# from logging import debug, info, warning, critical

# import pandas as pd
# import numpy as np

from params import GeneralParams as Params
from src import logger


def now():
    return str(datetime.datetime.now())[:19]


def setFileStruct():
    """check if all required folders OK else mkdir """

    logger.debug("called")

    # list files
    files = os.listdir()

    # check files
    for d in ["data", "logs", "tmp"]:
        if d not in files:
            logger.error("{d} not in general struct, lets create it")
            os.mkdir(d)

    return 0
