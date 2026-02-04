"""
Stock Monitor.

Periodically checks stock prices
and triggers alerts when targets are met.
"""

import asyncio
from typing import Dict

from app.market.public_api import fetch_stock_data
from app.alerts.notifier import send_alert


class StockMonitor:
    """
    Background stock price monitor.
    """

    def __init__(self, watchlist: Dict[str, float], interval: int = 60):
        self.watchlist = watchlist
        self.interval = interval

    async def start(self) -> None:
        """Start monitoring loop."""
        while True:
            for symbol, target_price in list(self.watchlist.items()):
                stock_data = await fetch_stock_data(symbol)
                current_price = stock_data["market_price"]

                if current_price <= target_price:
                    send_alert(symbol, current_price, target_price)
                    del self.watchlist[symbol]

            await asyncio.sleep(self.interval)
