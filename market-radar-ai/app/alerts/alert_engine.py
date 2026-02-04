"""
Alert Engine.

Evaluates stock prices against watchlist
and triggers buy alerts.
"""

from typing import List, Dict

from app.analysis.funda_data_fetcher import fetch_fundamental_data


def evaluate_alerts(watchlist: List[Dict]) -> List[str]:
    """
    Check watchlist stocks and generate alerts.

    Args:
        watchlist (List[Dict]): Watched stocks

    Returns:
        List[str]: Alert messages
    """
    alerts = []

    for item in watchlist:
        symbol = item["symbol"]
        target = item["target_price"]

        data = fetch_fundamental_data(symbol)
        current_price = data["market_price"]

        if current_price <= target:
            alerts.append(
                f"🚨 BUY ALERT: {symbol} hit ₹{current_price} (target ₹{target})"
            )

    return alerts
