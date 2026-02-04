"""
Watchlist Manager.

Handles user stock monitoring preferences
and persists them locally.
"""

import sqlite3
from typing import List, Dict

DB_PATH = "market_radar.db"


def init_watchlist() -> None:
    """Initialize watchlist table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS watchlist (
            symbol TEXT,
            target_price REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def add_to_watchlist(symbol: str, target_price: float) -> None:
    """Add stock to watchlist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO watchlist (symbol, target_price) VALUES (?, ?)",
        (symbol.upper(), target_price),
    )
    conn.commit()
    conn.close()


def get_watchlist() -> List[Dict]:
    """Return all watched stocks."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, target_price FROM watchlist")
    rows = cursor.fetchall()
    conn.close()

    return [{"symbol": r[0], "target_price": r[1]} for r in rows]
