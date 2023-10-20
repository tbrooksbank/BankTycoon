import logging

import pandas as pd

from utils.logging import log_config

logger = logging.getLogger(__name__)
logger = log_config(logger)


class CashAtBank:
    def __init__(self, settings, deals=None):
        if deals is None:
            cab = {'Counterparty': ['Bank of England'],
                   'Principal': [settings.initial_investment],
                   'Accrued_Interest': [0],
                   'Interest_Index': ['Fixed'],
                   'Interest_Rate': [0.0400]}
            self.deals = pd.DataFrame(data=cab)
        else:
            self.deals = deals

        logger.info(f"Cash at bank established with {len(self.deals)} deals.")

    def accrued_interest_time_step(self, index, row):
        accrued_interest = row['Accrued_Interest']
        accrued_interest_generated = (row['Principal'] * row['Interest_Rate']) / 360
        new_accrued_interest = accrued_interest + accrued_interest_generated
        self.deals.loc[index, 'Accrued_Interest'] = new_accrued_interest

    def time_step(self):
        for index, row in self.deals.iterrows():
            self.accrued_interest_time_step(index, row)

    def bs_values(self):
        principal = self.deals['Principal'].sum()
        accrued_interest = self.deals['Accrued_Interest'].sum()
        bsv = principal + accrued_interest
        return bsv
