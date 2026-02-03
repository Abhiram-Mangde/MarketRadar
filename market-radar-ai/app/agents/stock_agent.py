"""
StockAgent module.

Handles user commands related to stocks, 
provides technical/fundamental analysis,
and manages alerts/watchlist.
"""

import re
from app.analysis.technical import analyze_technical
from app.alerts.scheduler import AlertScheduler


class StockAgent:
    """
    Agent responsible for understanding stock commands
    and returning analysis or managing alerts.
    """

    def __init__(self):
        self.alert_scheduler = AlertScheduler()

    async def process(self, message: str) -> str:
        """
        Process user input and return a response.
        """
        msg = message.strip().lower()

        analyze_match = re.match(r"(analyze|show analysis) (\w+)", msg)
        if analyze_match:
            symbol = analyze_match.group(2).upper()
            return self._technical_analysis_response(symbol)

        monitor_match = re.match(r"(monitor|watch) (\w+) at (\d+(\.\d+)?)", msg)
        if monitor_match:
            symbol = monitor_match.group(2).upper()
            target_price = float(monitor_match.group(3))
            self.alert_scheduler.add_alert(symbol, target_price)
            return f"{symbol} added to watchlist at target price {target_price}"

        if "watchlist" in msg:
            return self.alert_scheduler.show_watchlist()

        return "Type 'Analyze <STOCK>' or 'Monitor <STOCK> at <PRICE>'"

    def _technical_analysis_response(self, symbol: str) -> str:
        """
        Generate technical analysis response for a stock symbol.
        """
        tech = analyze_technical(symbol)

        if tech.get("status") == "INSUFFICIENT_DATA":
            return f"{symbol}: {tech['message']}"

        return (
            f"{symbol} Technical Analysis:\n"
            f"- Price: {tech['price']}\n"
            f"- RSI: {tech['rsi']}\n"
            f"- SMA(20): {tech['sma_20']}\n"
            f"- SMA(50): {tech['sma_50']}\n"
            f"- Recommendation: {tech['recommendation']}\n"
            f"- Reasons: {', '.join(tech['reasons'])}"
        )
