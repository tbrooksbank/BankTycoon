import json
import logging
from pathlib import Path

from sqlalchemy.exc import IntegrityError
from sqlmodel import create_engine, Session, SQLModel

from database.models import BalanceSheet, ChartOfAccounts, Ledger
from utils.logging import log_config

DB_PATH = Path(__file__).parent / "data" / "database.db"
DB_URL = f"sqlite:///{DB_PATH}"

logger = logging.getLogger(__name__)
logger = log_config(logger)


def create_coa() -> None:
    """
    Function to create the chart of accounts from the json file. This should only happen
    on the initial creation of the database.
    """
    with open("database\chart_of_accounts.json", "r") as f:
        coa = json.load(f)

    engine = create_engine(DB_URL)
    with Session(engine) as session:
        for item in coa:
            session.add(ChartOfAccounts(**item))

        try:
            session.commit()
            logger.info("Chart of accounts created")
        except IntegrityError as e:
            logger.error(f"Error creating chart of accounts: {e}")

def create_db():
    models = [BalanceSheet, Ledger, ChartOfAccounts]

    # Create path if it doesn't exist:
    if not DB_PATH.parent.exists():
        DB_PATH.parent.mkdir()

    engine = create_engine(DB_URL)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables from models.py created")
