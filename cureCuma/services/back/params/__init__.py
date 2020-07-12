import os
import json
import logging
from logging import warning, info, debug, critical, error


class GeneralParams:
    """data storage object for general params (paths, logging etc etc) """

    # paths
    data = "data/"
    logs = "logs/"
    tmp = "tmp/"

    # app
    debug = bool(os.getenv("BACK_DEBUG", False))
    # host = os.getenv("BACK_HOST", "")
    port = int(os.getenv("BACK_PORT", 123))

    # tables
    messages_tn = os.getenv("MESSAGE_TABLENAME", "messages")
    locations_tn = os.getenv("LOCATION_TABLENAME", "locations")
    users_tn = os.getenv("USER_TABLENAME", "users")
    machines_tn = os.getenv("MACHINE_TABLENAME", "machines")
    tools_tn = os.getenv("TOOL_TABLENAME", "tools")
    inputs_tn = os.getenv("INPUT_TABLENAME", "inputs")
    companies_tn = os.getenv("COMPANY_TABLENAME", "companies")
    cumausers_tn = os.getenv("CUMAUSERS_TABLENAME", "cumausers")

    # database
    datadb = os.getenv("MYSQL_DATABASE", "cpmhkdb")
    db_user = os.getenv("MYSQL_USER", "curecuma")
    db_password = os.getenv("MYSQL_PASSWORD", "azerty")
    db_host = os.getenv("MYSQL_HOST", "mysql")
    db_port = os.getenv("MYSQL_PORT", "3306")

    # logging
    log_in_file = False  # if True log in file else in stdout
    logging_filemode = "w"  # ['a', 'w'] if "w" delete old file else append
    logging_level = os.getenv("BACK_LOGLEVEL", "INFO")
    logging_datefmt = "%Y-%m-%d %H:%M:%S"
    logging_format = "%(asctime)s | %(levelname)-8s | %(message)s %(funcName)s | %(lineno)d | %(module)s | %(filename)s"


def setBasicConfig(filename: str, params, ext: str = ".log"):
    """Update logging.basicConfig from params.py

    args :
        filename (str): the filename of the root script
        ext (str) : the extension - optional - defaut is .log"""

    # clean filename
    if ".py" in filename:
        filename = filename.replace(".py", "")

    # base for basiConfig
    logging_dict = {
        "level": getattr(logging, params.logging_level),
        "format": params.logging_format,
        "datefmt": params.logging_datefmt,
    }

    # logfile
    assert os.path.isdir(params.logs)
    logfile = f"{params.logs}{filename}{ext}"

    # if "w" as logging filemode rewrite logfile with header
    if (params.logging_filemode == "w") and params.log_in_file:
        open(logfile, "w").write("")

    # if log_in_file update basiConfig
    if params.log_in_file:
        logging_dict.update({"filename": logfile, "filemode": "a"})

    # basic config and logger
    logging.basicConfig(**logging_dict)
