"""
StockAgent for MarketRadar-AI.

Handles natural language stock commands such as:
- Analyze <STOCK>
- Monitor <STOCK> at <PRICE>
- Show my watchlist
"""

import asyncio
import re

from app.market.public_api import fetch_stock_data
from app.alerts.scheduler import AlertScheduler
from app.analysis.technical import analyze_technical
from app.analysis.fundamental import analyze_fundamentals
from app.ai.explanation_engine import explain_fundamentals
from app.nlu.command_parser import parse_command
from app.alerts.monitor import StockMonitor

class StockAgent:
    """
    AI-powered stock agent that parses commands,
    performs analysis, and manages alerts.
    """

    def __init__(self):
        self.alert_scheduler = AlertScheduler()
        self.watchlist = {}
        self.monitor = StockMonitor(self.watchlist)

        # Start the monitoring loop asynchronously
        asyncio.create_task(self.monitor.start())

    async def process(self, message: str) -> str:
        """
        Process user input and return a response.

        Args:
            message (str): User command

        Returns:
            str: Agent response
        """
        command = parse_command(message)

        if not command:
            return "Sorry, I didn't understand. Type 'help' for commands."

        action = command.get("action")

        if action == "ANALYZE":
            symbol = command["symbol"]
            stock_data = await fetch_stock_data(symbol)
            return self._format_analysis(symbol, stock_data)

        if action == "MONITOR":
            symbol = command["symbol"]
            target_price = command["target_price"]
            self.watchlist[symbol] = target_price
            return f"{symbol} added to watchlist at ₹{target_price}."

        if action == "SHOW_WATCHLIST":
            if not self.watchlist:
                return "Your watchlist is empty."
            return "\n".join(
                f"{s} → ₹{p}" for s, p in self.watchlist.items()
            )

        if action == "HELP":
            return (
                "Available commands:\n"
                "- Analyze <STOCK>\n"
                "- Monitor <STOCK> at <PRICE>\n"
                "- Show my watchlist"
            )

        return "Sorry, I didn't understand. Type 'help' for commands."

    def _format_analysis(self, symbol: str, stock_data: dict) -> str:
        """
        Combine fundamental and technical analysis
        into a human-readable response.
        """
        fundamentals = analyze_fundamentals(symbol)
        technicals = analyze_technical(symbol)

        fundamental_text = explain_fundamentals(fundamentals)

        if technicals.get("status") == "INSUFFICIENT_DATA":
            technical_text = technicals["message"]
        else:
            technical_text = (
                f"{symbol} Technical Analysis:\n"
                f"- Price: ₹{technicals['price']}\n"
                f"- RSI: {technicals['rsi']}\n"
                f"- SMA(20): {technicals['sma_20']}\n"
                f"- SMA(50): {technicals['sma_50']}\n"
                f"- Recommendation: {technicals['recommendation']}\n"
                f"- Reasons: {', '.join(technicals['reasons'])}"
            )

        return f"{fundamental_text}\n\n{technical_text}"
