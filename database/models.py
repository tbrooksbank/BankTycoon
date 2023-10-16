import datetime as dt

from sqlmodel import Field, SQLModel


class BalanceSheet(SQLModel, table=True):
    bs_category: str = Field(index=True, unique=True)
    bs_class: str = Field(index=True, unique=True)
    bs_account: str = Field(primary_key=True)
    balance: float


class Ledger(SQLModel, table=True):
    date: dt.date = Field(primary_key=True)
    bs_account: str = Field(primary_key=True)
    amount: float


class ChartOfAccounts(SQLModel, table=True):
    bs_category: str = Field(index=True)
    bs_class: str = Field(index=True)
    bs_account: str = Field(primary_key=True)
    sort_order: int
