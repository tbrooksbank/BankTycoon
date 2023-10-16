# Bank Tycoon

## Installation
With a terminal in the directory of the project run the following commands.

```cmd
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python database/create.py
```

## Game Idea
Democracy 3 style text and gui based bank management game with realistic regulation

Python coded with tkinkter gui and possibly some kind of db for game data in future 

## Core concepts
main.py runs the game

game_state.py contains the core data and detailed records, this object represents the players bank

settings.py contains the game settings these are imported to all classes and are defaulted for now but in time 
will be editable from the gui 

## Other Concepts

### Core_Data
balance_sheet.py contains the banks balance sheet, this is a summary of the ledger

ledger.py contains all monetary transactions and is combined with the chart of accounts to build the balance sheet

the_bank.py container class to hold all Core_Data and Detailed_Records classes

### Detailed_Records
In time will be one class set up file for all key concepts e.g staff, customer deposits, products

capital.py holds capital instruments of the bank

cash_at_bank.py holds all cash at banks

### Reference_Files
chart_of_accounts.json lookup table for balance sheet structure all accounts used in the ledger need an entry here

### saves 
Placeholder for game saves