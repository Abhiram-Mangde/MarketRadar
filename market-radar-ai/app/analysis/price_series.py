"""
Price Series Provider.

Provides historical price data for stocks.
Currently mocked, replaceable with free APIs later.
"""

from typing import List


def get_price_series(symbol: str, days: int = 30) -> List[float]:
    """
    Return historical closing prices.

    Args:
        symbol (str): Stock symbol
        days (int): Number of days

    Returns:
        List[float]: Closing prices
    """
    # Mocked NSE-style prices
    base_price = 86.0
    return [base_price + (i % 5 - 2) for i in range(days)]
