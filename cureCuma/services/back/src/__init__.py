import os
import time
import datetime
import logging

from flask import Flask, escape, request, render_template, session

# from flask_bcrypt import Bcrypt

from params import GeneralParams as Params
from params import setBasicConfig


setBasicConfig(os.getenv("SERVICE_NAME", "ipython"), Params)
logger = logging.getLogger()


from src.utils import setFileStruct
from src.config import Config
from src.model.utils import (
    wait_sql_up,
    create_table_if_needed,
    create_table,
    feed_if_empty,
)

# bcrypt = Bcrypt()


def create_app(config_class=Config):
    """create the app"""

    logger.debug("called")
    logger.debug(Params.__dict__)

    # create table if needed
    setFileStruct()
    wait_sql_up()
    create_table()
    feed_if_empty()

    # init app
    app = Flask(__name__)
    app.config.from_object(Config)
    # bcrypt.init_app(app)

    # # import routes
    from src.routes.users import users
    from src.routes.machines import machines

    # from src.routes.learnybox import webdownwebdownwebdown
    # from src.routes.db import db
    # from src.routes.subscriber import subscriber
    # from src.routes.woocommerce import woocommerce

    # # register
    app.register_blueprint(users)
    app.register_blueprint(machines)
    # app.register_blueprint(learnybox)
    # app.register_blueprint(db)
    # app.register_blueprint(subscriber)
    # app.register_blueprint(woocommerce)

    return app
