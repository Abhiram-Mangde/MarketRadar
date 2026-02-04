"""
Financial Ratios Calculator.

Contains helper functions to compute
common fundamental ratios.
"""


def price_to_earnings(price: float, eps: float) -> float:
    """Calculate P/E ratio."""
    return round(price / eps, 2) if eps > 0 else 0.0


def price_to_book(price: float, book_value: float) -> float:
    """Calculate P/B ratio."""
    return round(price / book_value, 2) if book_value > 0 else 0.0


def debt_to_equity(debt: float, equity: float) -> float:
    """Calculate Debt-to-Equity ratio."""
    return round(debt / equity, 2) if equity > 0 else 0.0


def profitability_score(roe: float) -> str:
    """Score profitability using ROE."""
    if roe >= 0.20:
        return "Strong"
    if roe >= 0.12:
        return "Moderate"
    return "Weak"
