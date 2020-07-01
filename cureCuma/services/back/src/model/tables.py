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
    Text,
)

from sqlalchemy.ext.declarative import declarative_base

from params import GeneralParams as Params

# from src.model.dB import engine, Base
from src.model import engine, Base, Session


class User(Base):

    __table__ = Table(
        Params.user_tablename,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime),  # 2020-01-01 00:00:00
        Column("email", String(50)),  # alex@duei.fr
        Column("pseudo", String(50)),  # alexCPMHK
        Column("password", String(50)),  # azerty
        Column("firstname", String(50)),  # alexandre
        Column("lastname", String(50)),  # gazagnes
        Column("phone", String(50)),  #  + 33 6 43 00 46 26
        Column("admin", Integer),  # 1 or 0
    )

    def __repr__(self):
        return f"{self.id} - {self.email} - {self.date}"


class Machnine(Base):

    __table__ = Table(
        Params.machine_tablename,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("email", String(50)),  # fent67@cuma.fr
        Column("plaque", String(50)),  # CZEH Z331
        Column("constructor", String(50)),  # FENT
        Column("model", String(50)),  # 850
        Column("_type", Integer),  # tracteur
    )

    def __repr__(self):
        return f"{self.id} - {self.email} - {self.date}"

