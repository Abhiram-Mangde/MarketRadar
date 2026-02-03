# app/market/public_api.py

import asyncio
import random

async def fetch_stock_data(symbol: str) -> dict:
    """
    Mock function to simulate fetching stock data from NSE/BSE.
    Replace with real API calls later.
    """
    await asyncio.sleep(0.5)  # Simulate network latency

    trends = ["Uptrend 📈", "Downtrend 📉", "Sideways ➖"]
    recommendations = ["Buy", "Hold", "Sell"]

    return {
        "symbol": symbol,
        "price": round(random.uniform(50, 1500), 2),
        "trend": random.choice(trends),
        "rsi": round(random.uniform(30, 70), 2),
        "recommendation": random.choice(recommendations)
    }
