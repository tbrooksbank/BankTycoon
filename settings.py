class settings(object):
    """Class to hold game settings"""
    def __init__(self, initial_investment=None, capital_premium_ratio=None,
                 base_rate=None):
        if initial_investment is None:
            self.initial_investment = 50000000
        else:
            self.initial_investment = initial_investment
        if capital_premium_ratio is None:
            self.capital_premium_ratio = 0.1
        else:
            self.capital_premium_ratio = capital_premium_ratio
        if base_rate is None:
            self.base_rate = base_rate
        else:
            self.base_rate = 0.04
        self.days = 30
        self.months = 12
        self.year = 2020
        self.days_in_year = self.days*self.months