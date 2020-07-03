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
        Params.users_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column(
            "created", String(20), nullable=False, default=""
        ),  # 2020-01-01 00:00:00
        Column("email", String(50), nullable=False),  # alex@duei.fr
        Column("pseudo", String(50), nullable=False),  # alexCPMHK
        Column("password", String(50), nullable=False),  # azerty
        Column("firstname", String(50), nullable=False, default=""),  # alexandre
        Column("lastname", String(50), nullable=False, default=""),  # gazagnes
        Column("phone", String(50), nullable=False, default=""),  #  + 33 6 43 00 46 26
        Column("admin", Integer, nullable=False, default=0),  # 1 or 0
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class Machine(Base):

    __table__ = Table(
        Params.machines_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        # Column("email", String(50)),  # fent67@cuma.fr
        Column("plaque", String(50), nullable=False),  # CZEH Z331
        Column("constructor", String(50), nullable=False, default=""),  # FENT
        Column("model", String(50), nullable=False, default=""),  # 850
        Column("_type", String(50), nullable=False, default=""),  # tracteur
        Column(
            "acquisition", String(20), nullable=False, default=""
        ),  # 2020-01-01 00:00:00
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())
