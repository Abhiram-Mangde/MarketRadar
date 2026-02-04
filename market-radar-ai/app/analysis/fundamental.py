"""
Fundamental Analysis Engine.

Combines raw financial data and computed ratios
to produce a clean investment-oriented summary.
"""

from typing import Dict

from app.analysis.funda_data_fetcher import fetch_fundamental_data
from app.analysis.financial_ratios import (
    price_to_earnings,
    price_to_book,
    debt_to_equity,
    profitability_score,
)


def analyze_fundamentals(symbol: str) -> Dict:
    """
    Perform fundamental analysis for a stock.

    Args:
        symbol (str): Stock symbol (NSE/BSE)

    Returns:
        Dict: Fundamental analysis summary
    """
    data = fetch_fundamental_data(symbol)

    pe = price_to_earnings(data["market_price"], data["eps"])
    pb = price_to_book(data["market_price"], data["book_value"])
    de = debt_to_equity(data["debt"], data["equity"])
    profit_score = profitability_score(data["roe"])

    return {
        "symbol": data["symbol"],
        "market_price": data["market_price"],
        "ratios": {
            "pe_ratio": pe,
            "pb_ratio": pb,
            "de_ratio": de,
            "roe": data["roe"],
            "dividend_yield": data["dividend_yield"],
        },
        "assessment": {
            "profitability": profit_score,
            "valuation": "Undervalued" if pe < 12 else "Fairly Valued",
            "risk": "High" if de > 1 else "Moderate",
        }
    }
