import os
import time

from src import logger
from params import GeneralParams as Params

import pandas as pd

from src.model.tables import *


def create_table():
    "create tables"

    logger.debug("called")
    Base.metadata.create_all(engine)


def create_table_if_needed():
    """create tables if no exists  """

    logger.debug("called")

    existing_tables = show_tables()
    logger.warning(f"existing tables : {existing_tables} ({type(existing_tables)}) ")

    # if not (Params.newsletter_tablename in existing_tables):
    #     logger.warning("ask for create table")
    create_table()


# def rm_db():

#     logger.debug("called")

#     db_filename = Params.data + Params.datadb + ".db"
#     if os.path.isfile(db_filename):
#         os.remove(db_filename)


def show_tables():
    """perform and cast a true show tables"""

    rr = engine.execute("show tables").fetchall()
    if len(rr):
        rr = list(rr[0])

    return rr


def test_sql_up():
    """test a dummy call """

    logger.debug("called")
    try:
        existing_tables = show_tables()
        logger.warning(f"existing_tables is {existing_tables} ")
        return 0

    except Exception as e:
        return e


def wait_sql_up(n_times=20, raiser=True):
    """test sql until Ok or not """

    logger.debug("called")

    for _ in range(n_times):
        error_connection = test_sql_up()
        if error_connection:
            time.sleep(2)
        else:
            return 0
    if raiser:
        raise ConnectionError(error_connection)
    else:
        return "SQL is not up"


# def clean_tables():
#     """ """

#     logger.debug("called")

#     from src.model.tables import Base, Transaction, Sale, Membre, engine
#     from src.model import Session

#     # delete previous tab
#     sess = Session()
#     sess.query(Sale).delete()
#     sess.commit()
#     sess.query(Transaction).delete()
#     sess.commit()
#     sess.query(Membre).delete()
#     sess.commit()

#     sess.close()


# def drop_tables():
#     """ """

#     logger.debug("called")
#     from src.model.tables import Base, Transaction, Sale, Membre, engine
#     from src.model import Session

#     Base.metadata.drop_all(
#         bind=engine, tables=[Transaction.__table__, Sale.__table__, Member.__table__]
#     )


def feed_if_empty():
    """feed with dummy values if empty tables  """

    logger.info("called")
    create_data_if_needed("users", User)
    create_data_if_needed("machines", Machine)


def create_data_if_needed(filename, TableObj):
    """feed with dummy data  """

    logger.info("called")
    # session
    sess = Session()
    # user / list return 0 if needed
    result = sess.query(TableObj).all()
    if len(result):
        return 0
    # read cvs
    df = pd.read_csv(Params.data + f"src/{filename}.csv")
    objs = [ser.to_dict() for _, ser in df.iterrows()]
    # make Users
    objs = [TableObj(**obj) for obj in objs]
    # add
    for obj in objs:
        try:
            sess.add(obj)
            sess.commit()
        except Exception as e:
            logger.error(e)
            sess.rollback()
    # close sess
    sess.close()
    return 0
