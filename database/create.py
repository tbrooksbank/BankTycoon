import json
from pathlib import Path

from sqlmodel import create_engine, Session, SQLModel

from database.models import BalanceSheet, ChartOfAccounts, Ledger

DB_PATH = Path(__file__).parent / "data" / "database.db"
DB_URL = f"sqlite:///{DB_PATH}"


def create_coa() -> None:
    """
    Function to create the chart of accounts from the json file. This should only happen
    on the initial creation of the database.
    """
    with open("chart_of_accounts.json", "r") as f:
        coa = json.load(f)

    engine = create_engine(DB_URL)
    with Session(engine) as session:
        for item in coa:
            session.add(ChartOfAccounts(**item))
        session.commit()


if __name__ == "__main__":
    models = [BalanceSheet, Ledger, ChartOfAccounts]

    # Create path if it doesn't exist:
    if not DB_PATH.parent.exists():
        DB_PATH.parent.mkdir()

    engine = create_engine(DB_URL)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    create_coa()
