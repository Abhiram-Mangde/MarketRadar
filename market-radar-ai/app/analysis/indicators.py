"""
Technical Indicators.

Contains implementations for common
technical analysis indicators.
"""

from typing import List


def simple_moving_average(prices: List[float], period: int) -> float:
    """Calculate SMA."""
    return round(sum(prices[-period:]) / period, 2)


def exponential_moving_average(prices: List[float], period: int) -> float:
    """Calculate EMA."""
    k = 2 / (period + 1)
    ema = prices[0]
    for price in prices[1:]:
        ema = price * k + ema * (1 - k)
    return round(ema, 2)


def relative_strength_index(prices: List[float], period: int = 14) -> float:
    """Calculate RSI."""
    gains = []
    losses = []

    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        if delta > 0:
            gains.append(delta)
        else:
            losses.append(abs(delta))

    avg_gain = sum(gains[-period:]) / period if gains else 0
    avg_loss = sum(losses[-period:]) / period if losses else 1

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)
