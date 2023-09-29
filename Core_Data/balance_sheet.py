import pandas as pd

class balance_sheet(object):
    bs_structure = {    "Category": [],
                        "Class": [],
                        "Account": [],
                        "Balance": []}

    def __init__(self):
        self.balance_sheet = pd.DataFrame(data=self.bs_structure)
        self.chart_of_accounts = pd.read_json(path_or_buf="Reference_Files/chart_of_accounts.json")

    def update_balance_sheet(self, ledger):
        ledger = ledger.get_ledger()
        bs_values = pd.DataFrame(ledger.groupby('Account')['Amount'].sum(), columns=['Amount'])
        full_bs = bs_values.merge(self.chart_of_accounts, on='Account', how='left')
        self.balance_sheet = full_bs

