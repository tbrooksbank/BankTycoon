import logging
import pandas as pd
import sqlite3
from sqlmodel import create_engine

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

    def time_step(self) -> None:
        """ Advances the data by 1 day, post's changes to ledger """
        engine = create_engine(DB_URL)

        sql = "SELECT * FROM CashAtBank"
        df = pd.read_sql(sql,engine)
        
        # Accrued Interest
        # TODO: Handle interest payment
        df['accrued_interest'] = df.apply(self.accrued_interest_time_step, axis=1)

        # Export Changes
        # TODO: Post changes to ledger
        df.to_sql("cashatbank", engine, if_exists="replace", index=False)