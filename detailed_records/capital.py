import logging

import pandas as pd

from utils.logging import log_config

logger = logging.getLogger(__name__)
logger = log_config(logger)


class Capital:
    def __init__(self, settings, deals=None):
        """Initializer, if fed a deals df from load file will use that else will follow bank establishment logic"""
        if deals is None:
            cap = {'Counterparty': ["Investors", "Investors"],
                   'Account': ["Paid Up Share Capital", "Share Premium"],
                   'Amount': [(settings.initial_investment * settings.capital_premium_ratio),
                              (settings.initial_investment * (1 - settings.capital_premium_ratio))]}
            self.deals = pd.DataFrame(data=cap)
        else:
            self.deals = deals

        logger.info(f"Capital established with {len(self.deals)} deals.")
