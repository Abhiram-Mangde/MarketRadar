# app/agents/stock_agent.py

import asyncio
import re
from app.market.public_api import fetch_stock_data
from app.alerts.scheduler import AlertScheduler

class StockAgent:
    """
    Stock Agent for MarketRadar-AI
    - Understands commands like:
        - Analyze <Stock>
        - Monitor <Stock> at <price>
        - Show my watchlist
    - Returns fundamental & technical insights
    - Adds alerts to scheduler
    """

    def __init__(self):
        self.alert_scheduler = AlertScheduler()

    async def process(self, message: str) -> str:
        msg = message.strip().lower()

        # Command: Analyze <Stock>
        analyze_match = re.match(r"(analyze|show analysis) (\w+)", msg)
        if analyze_match:
            symbol = analyze_match.group(2).upper()
            stock_data = await fetch_stock_data(symbol)
            return self._format_analysis(stock_data)

        # Command: Monitor <Stock> at <Price>
        monitor_match = re.match(r"(monitor|watch) (\w+) at (\d+(\.\d+)?)", msg)
        if monitor_match:
            symbol = monitor_match.group(2).upper()
            target_price = float(monitor_match.group(3))
            self.alert_scheduler.add_alert(symbol, target_price)
            return f"{symbol} added to your watchlist at target price {target_price}."

        # Command: Show watchlist
        if "watchlist" in msg:
            return self.alert_scheduler.show_watchlist()

        # Help fallback
        if "help" in msg:
            return (
                "Commands:\n"
                "- Analyze <Stock> : Get fundamental & technical analysis\n"
                "- Monitor <Stock> at <Price> : Add stock to watchlist\n"
                "- Show my watchlist : See current alerts"
            )

        return "Sorry, I didn't understand. Type 'help' for commands."

    def _format_analysis(self, stock_data: dict) -> str:
        """
        Converts stock_data dict into human-readable string.
        """
        if not stock_data:
            return "Stock data not found. Please check the symbol."

        return (
            f"{stock_data['symbol']} Analysis:\n"
            f"- Price: {stock_data['price']}\n"
            f"- Trend: {stock_data['trend']}\n"
            f"- RSI: {stock_data['rsi']}\n"
            f"- Recommendation: {stock_data['recommendation']}"
        )
