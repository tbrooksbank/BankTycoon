import logging
import pandas as pd
import sqlite3

from database.create import DB_URL

from utils.logging import log_config

logger = logging.getLogger(__name__)
logger = log_config(logger)


class cash_at_bank:
    def __init__(self):
        pass

    def accrued_interest_time_step(self, df, index, row) -> pd.DataFrame:
        """ Handles accrued interest component of time stepping """
        accrued_interest = row['accrued_interest']
        accrued_interest_generated = (row['principal'] * row['interest_rate']) / 360
        new_accrued_interest = accrued_interest + accrued_interest_generated
        df.loc[index, 'accrued_interest'] = new_accrued_interest
        return df

    def time_step(self) -> None:
        "Advances the data by 1 day"
        sql = "SELECT * FROM CashAtBank"
        conn = sqlite3.connect("database/data/database.db")
        df_org = pd.read_sql(sql,conn)
        
        #Accrued Interest
        # TODO: Handle interest payment
        for index, row in df_org.iterrows():
            df_new = self.accrued_interest_time_step(df_org, index, row)
        print(df_new)
        
        # TODO: Post changes to ledger