import logging
from utils.logging import log_config
import sqlite3
import pandas as pd

from database.create import DB_PATH

logger = logging.getLogger(__name__)
logger = log_config(logger)

def balance_sheet_summary() -> None:
    "Prints to log various summary statistics on the balance sheet"
    sql = "SELECT * FROM BalanceSheet"
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(sql,conn)
    logger.info("Balance Sheet Summary")
    logger.info("---------------------")
    assets = df.loc[df['bs_category'] == "Assets", "balance"].sum()
    liabs = df.loc[df['bs_category'] == "Liabilities", "balance"].sum()
    equity = df.loc[df['bs_category'] == "Equity", "balance"].sum()
    bs_lines = len(df.index)
    logger.info(f"Total Assets = {assets}")
    logger.info(f"Total Liabilities = {liabs}")
    logger.info(f"Total Equity = {equity}")
    logger.info(f"Total Balance Sheet Lines = {bs_lines}")

def ledger_summary() -> None:
    "Prints to log various summary statistics on the ledger"
    sql = "SELECT * FROM Ledger"
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(sql,conn)
    postings = len(df.index)
    value = df["amount"].sum()
    abs_value = sum(df["amount"].abs())
    logger.info(f"Total postings to ledger - {postings}")
    logger.info(f"Total value of postings to ledger - {value}, should always be 0")
    logger.info(f"Total absolute value of postings to ledger - {abs_value}")

def cash_at_bank_summary() -> None:
    """ Prints to log various summary statistics on cash at bank """
    sql = "SELECT * FROM CashAtBank"
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(sql,conn)
    deals = len(df.index)
    principal = df["principal"].sum()
    accrued_interest = df["accrued_interest"].sum()
    logger.info(f"Total Deals in cash at bank - {deals}")
    logger.info(f"Total Principal in cash at bank - {principal}")
    logger.info(f"Total Accrued Interest in cash at bank - {accrued_interest}")