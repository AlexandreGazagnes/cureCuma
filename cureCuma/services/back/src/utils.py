import os
import requests
import pprint
from pprint import pformat

# import sys
# import subprocess
# from logging import debug, info, warning, critical

# import pandas as pd
# import numpy as np

from params import GeneralParams as Params
from src import logger

# from src.model import Db


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

