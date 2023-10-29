from pathlib import Path
import logging
from utils.logging import log_config
import datetime as dt

from gamestate import GameState
from settings import Settings
import testing_output

from database.create import DB_PATH

logger = logging.getLogger(__name__)
logger = log_config(logger)

logger.info("main.py started")

settings = Settings()
logger.info("Settings Class Initialised")
game = GameState()
logger.info("Game State Initialised")

if DB_PATH.exists():
    DB_PATH.unlink()
    logger.info("Database already exists, Deleting")
import database.create
database.create.create_db()
database.create.create_coa()

game.bank.establish_bank(settings)
logger.info("Bank Established")

testing_output.balance_sheet_summary()
testing_output.ledger_summary()
testing_output.cash_at_bank_summary()

date = dt.date(2020, 1, 1)
for _ in range(5):
    date += dt.timedelta(days=1)
    game.bank.cash_at_bank.time_step(date)
    testing_output.balance_sheet_summary()
    testing_output.ledger_summary()
    testing_output.cash_at_bank_summary()
