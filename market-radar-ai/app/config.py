# app/config.py

# TCP Server Settings
TCP_HOST = "0.0.0.0"
TCP_PORT = 9000
MAX_CLIENTS = 5

# Stock Market API Settings (Free Public API Example)
MARKET_API_BASE_URL = "https://www.nseindia.com/api/quote-equity?symbol={symbol}"
API_TIMEOUT = 5  # seconds

# Watchlist / Database
WATCHLIST_DB_PATH = "app/storage/watchlist.db"

# Alert Check Interval
ALERT_CHECK_INTERVAL = 60  # seconds

# General Settings
DEBUG = True