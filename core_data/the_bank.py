import logging

from sqlalchemy.exc import IntegrityError
from sqlmodel import create_engine, Session

from database.create import DB_URL
from database.models import Ledger, CashAtBank
from detailed_records.capital import Capital
from detailed_records.cash_at_bank import cash_at_bank
from utils.logging import log_config

logger = logging.getLogger(__name__)
logger = log_config(logger)


class Bank:
    def __init__(self):
        self.cash_at_bank = None
        self.capital = None

    def establish_bank(self, settings):
        self.cash_at_bank = cash_at_bank()
        self.capital = Capital(settings)
        initial_investment = settings.initial_investment
        capital_premium_ratio = settings.capital_premium_ratio
        logger.info(f"Establishing bank with initial investment of {initial_investment}")

        # Create the initial ledger entries:
        engine = create_engine(DB_URL)
        with Session(engine) as session:
            start_date = settings.date
            session.add_all(
                [
                    Ledger(date=start_date, bs_account="Bank of England Reserve Account", amount=-initial_investment),
                    CashAtBank(counterparty="Bank of England", principal=initial_investment, accrued_interest=0, interest_rate=0.0400),
                    Ledger(
                        date=start_date, bs_account="Paid Up Share Capital",
                        amount=(initial_investment * capital_premium_ratio)
                    ),
                    Ledger(
                        date=start_date, bs_account="Share Premium",
                        amount=(initial_investment * (1 - capital_premium_ratio))
                    )
                ]
            )
            try:
                session.commit()
                logger.info(f"Initial ledger entries created for {start_date}")
            except IntegrityError as e:
                logger.error(f"Error creating initial ledger entries: {e}")
