import os

# import sqlite3
import datetime

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select, text

from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    Float,
    Integer,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

from params import GeneralParams as Params
from src import logger

# from src.model.db import Db


txt = f"mysql+pymysql://{Params.db_user}:{Params.db_password}@{Params.db_host}:{Params.db_port}/{Params.datadb}"
logger.warning(f"txt is {txt} ")

engine = create_engine(txt)
logger.warning(f"engine is {engine} ")

Base = declarative_base(engine)
logger.warning(f"Base is {Base} ")

Session = sessionmaker(bind=engine)
logger.warning(f"Session is {Session} ")
