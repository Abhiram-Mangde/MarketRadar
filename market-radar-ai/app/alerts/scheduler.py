# app/alerts/scheduler.py

import asyncio
from app.market.public_api import fetch_stock_data

class AlertScheduler:
    """
    Maintains a watchlist and checks stock prices asynchronously.
    """

    def __init__(self):
        self.watchlist = []  # Each entry: {"symbol": str, "target": float, "triggered": bool}
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self._alert_loop())

    def add_alert(self, symbol: str, target_price: float):
        self.watchlist.append({"symbol": symbol, "target": target_price, "triggered": False})

    def show_watchlist(self):
        if not self.watchlist:
            return "Your watchlist is empty."
        lines = []
        for item in self.watchlist:
            status = "Triggered ✅" if item["triggered"] else "Pending ⏳"
            lines.append(f"{item['symbol']} - Target: {item['target']}, Status: {status}")
        return "\n".join(lines)

    async def _alert_loop(self):
        """
        Background loop that checks stock prices every 60 seconds.
        """
        while True:
            if self.watchlist:
                for item in self.watchlist:
                    if item["triggered"]:
                        continue
                    stock_data = await fetch_stock_data(item["symbol"])
                    current_price = stock_data["price"]
                    if current_price >= item["target"]:
                        print(f"[ALERT] {item['symbol']} has reached target price {item['target']}! Current: {current_price}")
                        item["triggered"] = True
            await asyncio.sleep(60)  # Check every 60 seconds
