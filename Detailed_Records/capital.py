import pandas as pd

class capital(object):
    def __init__(self, settings, deals=None):
        """Initializer, if fed a deals df from load file will use that else will follow bank establishment logic"""
        if deals is None:
            cap = {'Counterparty': ["Investors","Investors"],
                   'Account': ["Paid Up Share Capital", "Share Premium"],
                   'Amount': [(settings.initial_investment*settings.capital_premium_ratio),
                              (settings.initial_investment*(1-settings.capital_premium_ratio))]}
            self.deals = pd.DataFrame(data=cap)
        else:
            self.deals = deals