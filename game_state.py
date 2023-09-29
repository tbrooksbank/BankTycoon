from Core_Data import the_bank
import settings

settings = settings.settings()

class game_state(object):
    """class to hold the current game state, exporting this creates the save files"""
    def __init__(self, bank=None):
        if bank is None:
            self.bank = the_bank.bank()
        else:
            self.bank = bank

    def time_step(self):
        #Update Detailed files
        self.banks.time_step()

        #Update Balance Sheet
        self.bs_update()

    def pl_update(self):
        #to-do
        Return

    def bs_update(self):
        self.balance_sheet.loc[0,'Value'] = self.banks.bs_values()

    def save_game(self):
        return

    def create_save_files(self):
        return