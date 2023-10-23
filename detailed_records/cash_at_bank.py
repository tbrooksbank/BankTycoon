import logging
import pandas as pd
import sqlite3
import datetime as dt
from sqlmodel import create_engine, Session
from sqlalchemy.exc import IntegrityError

from database.create import DB_URL 
from database.models import Ledger, CashAtBank

from utils.logging import log_config

logger = logging.getLogger(__name__)
logger = log_config(logger)


class cash_at_bank:
    def __init__(self):
        pass

    def accrued_interest_time_step(self, row) -> pd.DataFrame.apply:
        """ Handles accrued interest component of time stepping """
        accrued_interest_generated = (row['principal'] * row['interest_rate']) / 360
        new_accrued_interest = row['accrued_interest'] + accrued_interest_generated
        return new_accrued_interest

    def ledger_postings(self, old, new, date) -> None:
        """ Takes two cash at bank dataframes and calculates the differnces then posts to the ledger """
        engine = create_engine(DB_URL)

        principal_change = new['principal'].sum() - old['principal'].sum()
        accrued_interest_change = new['accrued_interest'].sum() - old['accrued_interest'].sum()
        # TODO: Add calc for interest payments

        # TODO: Handle Global dates
        with Session(engine) as session:
            session.add_all(
                [
                    Ledger(date=date, bs_account="Bank of England Reserve Account", amount=principal_change),
                    Ledger(date=date, bs_account="BofE Interest Income", amount=accrued_interest_change),
                    Ledger(date=date, bs_account="BofE Interest Receivable", amount=accrued_interest_change)
                ]
            )
            try:
                session.commit()
                logger.info(f"Cash at Bank ledger entries created for {date}")
            except IntegrityError as e:
                logger.error(f"Error creating cash at bank ledger entries: {e}")


    def time_step(self, date) -> None:
        """ Advances the data by 1 day, post's changes to ledger """
        engine = create_engine(DB_URL)

        sql = "SELECT * FROM CashAtBank"
        df = pd.read_sql(sql,engine)
        df_new = df
        
        # Accrued Interest
        # TODO: Handle interest payment
        df_new['accrued_interest'] = df_new.apply(self.accrued_interest_time_step, axis=1)

        # Export Changes
        df_new.to_sql("cashatbank", engine, if_exists="replace", index=False)

        # TODO: Post changes to ledger
        self.ledger_postings(df, df_new, date)