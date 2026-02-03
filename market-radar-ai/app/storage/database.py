import sqlite3
from pathlib import Path

DB_PATH = Path("app/storage/market_radar.db")

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)
