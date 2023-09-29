import pandas as pd

class ledger(object):
    def __init__(self, ledger=None):
        if ledger is None:
            gl = {'Day': [],
                  'Month': [],
                  'Year': [],
                  'Account': [],
                  'Amount': []}
            self.ledger = pd.DataFrame(data=gl)
        else:
            self.ledger = ledger

    def get_ledger(self):
        return self.ledger

    def add_to_ledger(self, transactions):
        for transaction in transactions:
            self.ledger.loc[len(self.ledger)] = transaction