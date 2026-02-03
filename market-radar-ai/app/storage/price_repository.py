from app.storage.database import get_connection

def save_price(symbol: str, price: float):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO prices (symbol, price) VALUES (?, ?)",
        (symbol, price)
    )

    conn.commit()
    conn.close()


def get_recent_prices(symbol: str, limit: int = 50):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT price FROM prices WHERE symbol = ? ORDER BY timestamp DESC LIMIT ?",
        (symbol, limit)
    )

    rows = cursor.fetchall()
    conn.close()

    return [r[0] for r in rows]
