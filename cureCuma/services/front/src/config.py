"""App configuration."""

import os
from os import environ, path

# from dotenv import load_dotenv

# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, ".env"))

# import redis


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = os.getenv("FRONT_SECRET_KEY", "azery")
    FLASK_APP = os.getgetenv("FRONT_FLASK_APP", "front")
    SESSION_COOKIE_NAME = os.getgetenv("SESSION_COOKIE_NAME", "cureCumaCookie")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Flask-Session
    # SESSION_TYPE = environ.get("SESSION_TYPE")
    # SESSION_REDIS = redis.from_url("redis://redis:6379")
    # SEND_FILE_MAX_AGE_DEFAULT = 0


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
