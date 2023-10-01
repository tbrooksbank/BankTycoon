import game_state
import settings
from tkinter import  *

settings = settings.settings()
game = game_state.game_state()

#game.bank.establish_bank(settings)

#print(game.bank.ledger.ledger.head())
#print(game.bank.balance_sheet.balance_sheet)
#print(game.bank.cash_at_bank.deals)
#print(game.bank.capital.deals)

# root window
root = Tk()
root.geometry('1920x1080')
root.title('BankTycoon')

# menubar
menubar = Menu(root)
root.config(menu=menubar)

# create file menu
file_menu = Menu(menubar, tearoff=0)

# function to display bank stats
def bank_info():
    data = game.bank.balance_sheet.balance_sheet
    n_rows = data.shape[0]
    n_cols = data.shape[1]
    col_names = data.columns
    
    for j, col in enumerate(col_names):
        text = Text(root, width=16, height = 1, bg = "#9BC2E6")
        text.grid(row=0, column=j)
        text.insert(INSERT, col)
    
    for i in range(n_rows):
        for j in range(n_cols):
            text = Text(root, width=16, height=1)
            text.grid(row=i+1, column=j)
            text.insert(INSERT, data.loc[i][j])

# add menu options
file_menu.add_command(label='Establish Bank', command=lambda: game.bank.establish_bank(settings))
file_menu.add_command(label='Bank Stats', command= lambda: bank_info())
file_menu.add_command(label='Exit', command=root.destroy)

# add menue to menubar
menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()