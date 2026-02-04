"""
Technical Analysis Engine.

Combines price data and indicators
to produce trading insights.
"""

from typing import Dict

from app.analysis.price_series import get_price_series
from app.analysis.indicators import (
    simple_moving_average,
    exponential_moving_average,
    relative_strength_index,
)


def analyze_technical(symbol: str) -> Dict:
    """
    Perform technical analysis for a stock.

    Args:
        symbol (str): Stock symbol

    Returns:
        Dict: Technical analysis summary
    """
    prices = get_price_series(symbol)

    sma_20 = simple_moving_average(prices, 20)
    ema_20 = exponential_moving_average(prices, 20)
    rsi = relative_strength_index(prices)

    signal = "Neutral"
    if rsi < 30:
        signal = "Oversold (Buy Zone)"
    elif rsi > 70:
        signal = "Overbought (Caution)"

    return {
        "symbol": symbol.upper(),
        "indicators": {
            "sma_20": sma_20,
            "ema_20": ema_20,
            "rsi": rsi,
        },
        "signal": signal,
    }
