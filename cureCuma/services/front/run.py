shebang = "#! /home/alex/Env/bin/python3"

from flask.cli import FlaskGroup

from src import logger
from src import create_app

# from utils.compile_scss import compile_scss


app = create_app()
