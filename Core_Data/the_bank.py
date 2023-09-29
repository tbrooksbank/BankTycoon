from Core_Data import ledger
from Core_Data import balance_sheet

class bank(object):
    def __init__(self):
        self.ledger = ledger.ledger(ledger=None)
        self.balance_sheet = balance_sheet.balance_sheet()

    def establish_bank(self, settings):
        initial_investment = settings.initial_investment
        capital_premium_ratio = settings.capital_premium_ratio
        ledger_entries =    [
                            [1,1,settings.year,"Bank of England Reserve Account",-initial_investment],
                            [1,1,settings.year,"Paid Up Share Capital",(initial_investment*capital_premium_ratio)],
                            [1,1,settings.year,"Share Premium",(initial_investment*(1-capital_premium_ratio))]
        ]
        self.ledger.add_to_ledger(ledger_entries)
        self.balance_sheet.update_balance_sheet(self.ledger)