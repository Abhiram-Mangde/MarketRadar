import asyncio
import random
from app.storage.price_repository import save_price

async def fetch_stock_data(symbol: str) -> dict:
    await asyncio.sleep(0.3)

    price = round(random.uniform(50, 1500), 2)

    save_price(symbol, price)

    return {
        "symbol": symbol,
        "price": price
    }
