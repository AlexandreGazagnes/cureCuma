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
# USER
####################################################


class User(Base):
    """User
    could be 3 things
    a real user
    root aka cureCuma
    a fake user relative to the account auto created"""

    __table__ = Table(
        Params.users_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("email", String(50), nullable=False, unique=True),  # alex@ei.fr
        Column("password", String(50), nullable=False,),  # azerty
        Column("category", Integer, nullable=False),  # human, account /subAccount
        Column("firstname", String(50),),  # alexandre
        Column("lastname", String(50),),  # gazagnes
        Column("phone", String(50),),  #  + 33 6 43 00 46 26
        Column("birthdate", String(20),),  # 20/11/1986
        Column("security_number", String(50),),  #  1 06.11.12.12.11
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class Message(Base):
    """just a standard message to be sent to any/some users 
    from root / curecuma to anyone
    from a user to an other
    from a user to an account group all members in Cuma case"""

    __table__ = Table(
        Params.messages_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("user_id", Integer, nullable=False),  # 1
        Column("title", String(50), nullable=False),  # hello
        Column("text", String(1000), nullable=False),  # mon premier message
        Column("destination", String(50),),  # all
        Column("category", String(50),),  # general
        Column("importance", Integer,),  # 0,1, or 2
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


####################################################
#   LOCATIONS
####################################################


class Location(Base):
    """any crop, constrcution land or earthpeice 
    a location is related to a real / fake user, somebody or a cuma 
    an employee shoul have a location
    """

    __table__ = Table(
        Params.locations_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("name", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("user_id", Integer, nullable=False),  # bonniere-devant
        Column("category", String(50), nullable=False,),  # parcel / Constrcutin
        Column("adress", String(50), nullable=False),  # route de bonniere
        Column("postcode", String(5), nullable=False),  # 45230
        Column("town", String(50), nullable=False),  # Chatillon-colligny
        Column("subtown", String(50), nullable=False),  # boniere
        Column("square", Float,),  # 10
        Column("latitude", Float,),  # 47.840
        Column("longitude", Float,),  # 2.8642
        Column("altitude", Integer,),  # 12
        Column("subcategory", String(50),),  # ???
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


####################################################
# ORGANISATION
####################################################


class Account(Base):
    """Account table 
    ABS class because no direct info expect plan id name
    no location for ie
    if just for one personn user_id refer to self and cpmpany_id refter to self if cuma user_id refer to a fake user auto created and company_id shoul be created"""

    __table__ = Table(
        Params.accounts_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("name", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("user_id", Integer, nullable=False),  # 1
        Column("company_id", Integer, nullable=False),  # personnel / cuma /
        Column("category", String(50), nullable=False),  # personnel / cuma /
        Column("plan", String(50), nullable=False),  # commercial plan
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class AccountUser:
    """all user for one or more cuma """

    __table__ = Table(
        Params.accountusers_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("user_id", Integer, nullable=False),
        Column("account_id", Integer, nullable=False),
        Column("adherent", Integer, nullable=False),
        Column("administrator", Integer, nullable=False),  # APP ADMI
        Column("executive", Integer, nullable=False),  # APP ADMI
        Column("manager", Integer, nullable=False),  # APP ADMI
        Column("role", String(50), nullable=False),
        Column("employee", Integer, nullable=False),
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


class Company(Base):
    """a Company
    the Administrative Entity
    """

    __table__ = Table(
        Params.companies_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("name", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("user_id", Integer, nullable=False),  # 1
        Column("location_id", Integer, nullable=False),  # 1
        Column("siret", String(50), nullable=False),
        Column("juridic", String(50),),
        # Column("category", String(50),),  # general
        Column("comments", String(500),),
        Column("active", Integer,),
    )

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

    def __repr__(self):
        return str(self.as_dict())


# class CompanyEmployee:
#     """a company """

#     pass


####################################################
# OBJECTS
####################################################


class Machine(Base):

    __table__ = Table(
        Params.machines_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("user_id", Integer, nullable=False),  # alexCPMHK
        Column("location_id", Integer, nullable=False),  # alexCPMHK
        Column("plaque", String(50), nullable=False, unique=True),  # CZEH Z331
        Column("constructor", String(50), nullable=False, default=""),  # FENT
        Column("model", String(50), nullable=False, default=""),  # 850
        Column("category", String(50), nullable=False,),  # tracteur
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


class Tool(Base):
    """A tool is a non selpowered mechanics sush as coupe, benne etc etc"""

    __table__ = Table(
        Params.tools_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("owner", Integer, nullable=False),  # alexCPMHK
        Column("location_id", Integer, nullable=False),  # alexCPMHK
        Column("pseudo", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("constructor", String(50), nullable=False, default=""),  # FENT
        Column("model", String(50), nullable=False, default=""),  # 850
        Column("category", String(50), nullable=False,),  # tracteur
        Column("submodel", String(50),),  #
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )


class Input(Base):
    """any input to use, fuel, engrais etc etc """

    __table__ = Table(
        Params.inputs_tn,
        Base.metadata,
        Column("id", Integer, primary_key=True),  # 0
        Column("created", DateTime, nullable=False,),  # 2020-01-01 00:00:00
        Column("owner", Integer, nullable=False),  # alexCPMHK
        Column("ref", String(50), nullable=False, unique=True),  # alexCPMHK
        Column("category", String(50), nullable=False),  # engrais
        Column("subcategory", String(50), nullable=False),  # engrais
        Column("in_category", String(50), nullable=False),  # alexCPMHK
        Column("in_id", Integer, nullable=False),
        Column("quantity_volume", Float, nullable=False),  # 0
        Column("quantity_unity", String(10), nullable=False),  # 0
        Column("construtor", String(50)),  # engrais
        Column("model", String(50),),  # engrais
        Column("comments", String(500),),  # a very beautifull crop
        Column("active", Integer,),  # 1
    )


####################################################
# IO / BUYS / SELL / USE
####################################################


# class ToolIO:
#     """A tool i"""

#     pass


# class InputIO:
#     """input buy, use and sales"""

#     pass


# class MachineIO:
#     """machine buy, use and sales"""

#     pass


####################################################
# PROCESS / WORK / ETC
####################################################


# class Project:
#     """a project is for 1 year, 1 parcel, 1 culture """

#     pass


# class Task:
#     """One task"""

#     pass


# class WorkContract:
#     """One or more Workcontract for one task but one per human """

#     pass


# class MachineUsage:
#     """One or more Rreservation for one task but one per human """

#     pass


####################################################
# METEOROLOGIE
####################################################


# class ParcelStation(Base):
#     __table__ = Table(
#         Params.parcelstation_tn,
#         Base.metadata,
#         Column("id", Integer, primary_key=True),  # 0
#         Column("date", DateTime, nullable=False,),  # 2020-01-01 00:00:00
#         # station
#         # temperature)
#     )

#     def as_dict(self):
#         return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

#     def __repr__(self):
#         return str(self.as_dict())


# class ParcelWeather(Base):
#     __table__ = Table(
#         Params.parcelweather_tn,
#         Base.metadata,
#         Column("id", Integer, primary_key=True),  # 0
#         Column("date", DateTime, nullable=False,),  # 2020-01-01 00:00:00
#         # station_id
#         # temperature
#         # rain
#         # sun
#         # atmPressure
#         # wind_forece
#         # wind_direction
#     )

#     def as_dict(self):
#         return {k: v for k, v in self.__dict__.items() if "_sa_instance_state" not in k}

#     def __repr__(self):
#         return str(self.as_dict())

