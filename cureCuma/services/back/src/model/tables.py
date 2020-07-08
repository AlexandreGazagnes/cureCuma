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
from src import logger


####################################################
# HUMAN
####################################################


class User(Base):
    """User"""

    __table__ = Table(
        Params.users_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("email", String(50), nullable=False, unique=True),  # alex@ei.fr
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("password", String(50), nullable=False,),  # azerty
        Column("admin", Integer, nullable=False, default=0),  # 1 or 0
        Column("status", String(50)),  # employe, propriaitaire etc
        Column("firstname", String(50),),  # alexandre
        Column("lastname", String(50),),  # gazagnes
        Column("phone", String(50),),  #  + 33 6 43 00 46 26
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


####################################################
# ORGANISATION
####################################################


class Cuma:
    """a Cuma"""

    pass


class CumaUser:
    """all user for one or more cuma """

    pass


class Company:
    """a company """

    pass


####################################################
# OBJECTS
####################################################


class Parcel(Base):
    """any crop, land or earthpeice """

    __table__ = Table(
        Params.parcels_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("owner", Integer, nullable=False),  # bonniere-devant
        Column("adress", String(50), nullable=False),  # route de bonniere
        Column("postcode", String(5), nullable=False),  # 45230
        Column("town", String(50), nullable=False),  # Chatillon-colligny
        Column("subtown", String(50), nullable=False),  # boniere
        Column("square", Float,),  # 10
        Column("lattitute", Float,),  # 47.840
        Column("longitude", Float,),  # 2.8642
        Column("altitude", Integer,),  # 12
        Column("ground", String(50),),  # normal
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
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
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("owner", Integer, nullable=False),  # alexCPMHK
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("plaque", String(50), nullable=False, unique=True),  # CZEH Z331
        Column("constructor", String(50), nullable=False, default=""),  # FENT
        Column("model", String(50), nullable=False, default=""),  # 850
        Column("type", String(50), nullable=False,),  # tracteur
        Column("oil_capacity", Integer, nullable=False,),  # 120
        Column("oil", Integer, nullable=False,),  # 80
        Column("kms", Integer, nullable=False,),  # tracteur
        Column("hours", Integer, nullable=False,),  # tracteur
        Column("submodel", String(50),),  #
        Column("auth_tools", String(500),),  # tracteur
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )

    def consume(self, oil, kms, hours):
        """reprsentaion of obj modification """

        logger.debug("called")

        self.hours += hours
        self.kms += kms
        self.oil -= oil
        if self.oil < 0:
            logger.critical(f"oil of Machine id {self.id} is {self.oil}")
            self.oil = 0

    def partial_refuel(self, oil):
        """partial refuell """

        logger.debug("called")

        self.oil += int(oil)
        if self.oil > self.oil_capacity:
            logger.critical(f"oil of Machine id {self.id} is {self.oil}")
            self.oil = self.oil_capacity

    def full_refuel(self):
        """reprsentaion of obj modification """

        logger.debug("called")

        self.oil = self.oil_capacity

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class Message:
    """just a standard message to be sent to any/some users """

    __table__ = Table(
        Params.messages_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("author", Integer, nullable=False),  # 1
        Column("title", String(50), nullable=False),  # hello
        Column("text", String(1000), nullable=False),  # mon premier message
        Column("destination", String(50),),  # all
        Column("category", String(50),),  # general
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class Tool:
    """A tool is a non selpowered mechanics sush as coupe, benne etc etc"""

    __table__ = Table(
        Params.machines_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("owner", Integer, nullable=False),  # alexCPMHK
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("constructor", String(50), nullable=False, default=""),  # FENT
        Column("model", String(50), nullable=False, default=""),  # 850
        Column("type", String(50), nullable=False,),  # tracteur
        Column("submodel", String(50),),  #
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )


class Input:
    """any input to use, fuel, engrais etc etc """

    __table__ = Table(
        Params.machines_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("owner", Integer, nullable=False),  # alexCPMHK
        Column("ref", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("type", String(50), nullable=False),  # engrais
        Column("subtype", String(50), nullable=False),  # engrais
        Column("is_in_type", String(50), nullable=False),  # engrais
        Column("quantity_volume", Float, nullable=False),  # 0
        Column("quantity_unity", String(10), nullable=False),  # 0
        Column("is_in_id", String(50),),  # engrais
        Column("construtor", String(50)),  # engrais
        Column("model", String(50),),  # engrais
        Column("type", String(50),),  # engrais
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )


####################################################
# IO / BUYS / SELL / USE
####################################################


class ToolIO:
    """A tool i"""

    pass


class InputIO:
    """input buy, use and sales"""

    pass


class MachineIO:
    """machine buy, use and sales"""

    pass


####################################################
# PROCESS / WORK / ETC
####################################################


class Project:
    """a project is for 1 year, 1 parcel, 1 culture """

    pass


class Task:
    """One task"""

    pass


class WorkContract:
    """One or more Workcontract for one task but one per human """

    pass


class MachineUsage:
    """One or more Rreservation for one task but one per human """

    pass


####################################################
# METEOROLOGIE
####################################################


class ParcelStation(Base):
    __table__ = Table(
        Params.parcelstation_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("date", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        # station
        # temperature)
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class ParcelWeather(Base):
    __table__ = Table(
        Params.parcelweather_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("date", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        # station_id
        # temperature
        # rain
        # sun
        # atmPressure
        # wind_forece
        # wind_direction
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())

