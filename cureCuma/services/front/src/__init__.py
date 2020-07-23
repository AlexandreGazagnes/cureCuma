import os
import sys
import logging
import secrets

from flask import Flask
from flask import render_template, redirect, escape, request, session
from flask_login import LoginManager
from flask_session import Session
from flask_bcrypt import Bcrypt

# from flask_scss import Scss


from params import GeneralParams as Params
from params import setBasicConfig


setBasicConfig(os.getenv("FRONT_SERVICE_NAME", "ipython"), Params)
logger = logging.getLogger()

from src.config import ProdConfig, DevConfig
from src.utils import setFileStruct
from src.register.routes import register

# replace by redis in next feature

# sess = Session()
bcrypt = Bcrypt()


def create_app(config_class=DevConfig):
    """make app """

    logger.debug("called")
    
    # sanity check
    logger.debug(Params.__dict__)
    setFileStruct()

    # app
    app = Flask(__name__)
    # config
    app.config.from_object(DevConfig)


    # plugin
    # sess.init_app(app)
    # bcrypt.init_app(app)

    # context manager
    with app.app_context():

        app.register_blueprint(register)

        return app
