from app.storage.database import get_connection
from app.market.public_api import fetch_stock_data
import asyncio

class AlertScheduler:

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self._alert_loop())

    def add_alert(self, symbol: str, target_price: float):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO watchlist (symbol, target_price) VALUES (?, ?)",
            (symbol, target_price)
        )

        conn.commit()
        conn.close()

    def show_watchlist(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT symbol, target_price, triggered FROM watchlist")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "Your watchlist is empty."

        return "\n".join(
            f"{r[0]} | Target: {r[1]} | {'Triggered' if r[2] else 'Pending'}"
            for r in rows
        )

    async def _alert_loop(self):
        while True:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT symbol, target_price FROM watchlist WHERE triggered = 0"
            )
            rows = cursor.fetchall()
            conn.close()

            for symbol, target in rows:
                stock = await fetch_stock_data(symbol)
                if stock["price"] >= target:
                    print(f"[ALERT] {symbol} reached {target}")
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE watchlist SET triggered = 1 WHERE symbol = ? AND target_price = ?",
                        (symbol, target)
                    )
                    conn.commit()
                    conn.close()

            await asyncio.sleep(60)
