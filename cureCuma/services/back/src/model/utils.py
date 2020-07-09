import os
import time

from src import logger
from params import GeneralParams as Params

import pandas as pd

from src.model.tables import *


class ModelUtils:
    """Model utils in one Class"""

    @staticmethod
    def boot(silent_raise=False):
        """manage all boot model ops """

        logger.debug("called")

        try:
            ModelUtils._wait_sql_up()
            ModelUtils._create_table()
            ModelUtils._feed_if_empty()
            return 0
        except Exception as e:
            if not silent_raise:
                raise e
            logger.error(e)
            return 1
        return 2

    @staticmethod
    def _create_table(silent_raise=True):
        """create tables"""

        logger.debug("called")

        try:
            Base.metadata.create_all(engine)
            return 0
        except Exception as e:
            if not silent_raise:
                raise e
            logger.error(e)
            return 1
        return 2

    @staticmethod
    def _show_tables(silent_raise=True):
        """perform and cast a true show tables"""

        logger.debug("called")

        # show tables
        try:
            rr = engine.execute("show tables").fetchall()
        except Exception as e:
            if not silent_raise:
                raise e
            logger.error(e)
            return -1

        # return list
        logger.warning(f"rr is {rr}")
        # TODO BE SURE OF THIS ONE

        try:
            if len(rr):
                rr = list(rr[0])
            return rr
        except Exception as e:
            if not silent_raise:
                raise e
            logger.error(e)
            return 1
        return 2

    @staticmethod
    def _test_sql_up(silent_raise=True):
        """test a dummy call """

        logger.debug("called")

        # get existing Tables
        try:
            existing_tables = ModelUtils._show_tables()
            logger.info(f"existing_tables is {existing_tables} ")
        except Exception as e:
            if not silent_raise:
                raise e
            logger.error(e)
            return -1

        if isinstance(existing_tables, list):
            return 1
        else:
            return 0
        return -2

    @staticmethod
    def _wait_sql_up(n_times=50, sleeper=4, silent_raise=False):
        """test sql until Ok or not """

        logger.debug("called")

        for n_time in range(n_times):
            # not connected wait
            if ModelUtils._test_sql_up() < 1:
                logger.info(f"for loop {n_time} db IS NOT up ")
                time.sleep(sleeper)
            # return
            else:
                logger.info(f"for loop {n_time} db IS up ")
                return 0

        # did not succed to conect to db
        error_str = f"SQL Db is not up  after {n_times} tries with sleep {sleeper} "
        if not silent_raise:
            raise ConnectionError(error_str)
        else:
            logger.error(error_str)
            return 1
        return 2

    @staticmethod
    def _feed_if_empty(silent_raise=True):
        """feed with dummy values if empty tables  """

        logger.info("called")
        ModelUtils._create_data_if_needed("users", User)
        ModelUtils._create_data_if_needed("machines", Machine)
        ModelUtils._create_data_if_needed("messages", Message)
        ModelUtils._create_data_if_needed("tools", Tool)
        ModelUtils._create_data_if_needed("locations", Location)
        ModelUtils._create_data_if_needed("inputs", Input)

    @staticmethod
    def _create_data_if_needed(filename, TableObj, silent_raise=True):
        """feed with dummy data  """

        logger.info("called")

        # session
        sess = Session()
        # user / list return 0 if needed
        result = sess.query(TableObj).all()
        if len(result):
            sess.close()
            return 0
        # read cvs
        df = pd.read_csv(Params.data + f"src/{filename}.csv")
        # make Obj for each
        objs = [TableObj(**ser.to_dict()) for _, ser in df.iterrows()]
        # add
        def add_commit(obj):
            try:
                sess.add(obj)
                sess.commit()
                return (1, None)
            except Exception as e:
                logger.error(e)
                sess.rollback()
                return (0, obj)

        # add_commit
        results = [add_commit(obj) for obj in objs]
        # compute stats
        rr = round(sum([i[0] for i in results]) * 100 / len(results), 2)
        # info log if needed
        logger.warning(f"bootstap for {filename} stat of success is {rr}% ")
        if rr < 99:
            errors = [i[1] for i in results if i[1]]
            logger.critical(f"bootstap for {filename} errors is {errors} ")

        # close sess
        sess.close()
        return 1


# def rm_db():

#     logger.debug("called")

#     db_filename = Params.data + Params.datadb + ".db"
#     if os.path.isfile(db_filename):
#         os.remove(db_filename)

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

# def create_table_if_needed(silent_raise=True):
#     """create tables if no exists  """

#     logger.debug("called")

#     # tables existanece
#     try:
#         existing_tables = show_tables()
#         logger.warning(
#             f"existing tables : {existing_tables} ({type(existing_tables)}) "
#         )
#         return 0
#     except Exception as e:
#         if not silent_raise:
#             raise e
#         logger.error(e)
#         return 1

#     # create tables
#     # if not (Params.newsletter_tablename in existing_tables):
#     #     logger.warning("ask for create table")
#     try:
#         create_table()
#         return 0
#     except Exception as e:
#         if not silent_raise:
#             raise e
#         logger.error(e)
#         return 2
