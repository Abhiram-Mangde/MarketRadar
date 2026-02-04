"""
Fundamental Data Fetcher.

Responsible for retrieving company financial data
from free public sources (mocked for now).
"""

from typing import Dict


def fetch_fundamental_data(symbol: str) -> Dict:
    """
    Fetch fundamental financial data for a given stock symbol.

    Args:
        symbol (str): NSE/BSE stock symbol (e.g., VEDL)

    Returns:
        Dict: Financial data including income, balance sheet, and market info
    """
    # Mocked data (replace with real API later)
    return {
        "symbol": symbol.upper(),
        "market_price": 86.0,
        "eps": 18.2,
        "book_value": 120.5,
        "net_profit": 22000,
        "revenue": 145000,
        "total_assets": 250000,
        "total_liabilities": 130000,
        "equity": 120000,
        "debt": 65000,
        "roe": 0.18,
        "dividend_yield": 0.06
    }
