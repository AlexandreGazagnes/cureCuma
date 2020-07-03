import secrets
from flask import Flask
from flask import render_template, redirect, escape, request, session
from flask_login import LoginManager
from flask_session import Session
from flask_bcrypt import Bcrypt

# from flask_scss import Scss


from params import GeneralParams as Params
from params import setBasicConfig


setBasicConfig(os.getenv("SERVICE_NAME", "ipython"), Params)
logger = logging.getLogger()

from src.config import ProdConfig, DevConfig
from src.utils import setFileStruct
from src.front import front

# replace by redis in next feature

sess = Session()
bcrypt = Bcrypt()


def create_app(config_class=DevConfig):
    """make app """

    logger.debug("called")
    # sanity check
    logger.debug(Params.__dict__)
    setFileStruct()
    # app
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    # plugin
    sess.init_app(app)
    # bcrypt.init_app(app)

    # context manager
    with app.app_context():

        app.register_blueprint(front)
        # from app.back import back

        # app.register_blueprint(back)
        # Scss(app)
        # Scss(app, static_dir="static/css", asset_dir="assets/scss")
        return app
