# MarketRadar-AI

**An AI-powered, TCP-based stock analysis and alerting platform for Indian equity markets (NSE/BSE).**  
This project demonstrates a **real-time stock analysis engine** with fundamental & technical insights, watchlist management, and event-driven alerts — all built with Python, async architecture, and free public APIs.

## Features

### Stock Analysis
- Fundamental insights (revenue, debt, ROE, etc.)
- Technical indicators (SMA, RSI, trends, support/resistance)
- AI-driven explanations in simple language

### Watchlist & Alerts
- Add stocks to monitor with target price
- Background tasks check live prices
- Alerts triggered when target price is reached
- Persistent watchlist storage (SQLite)

### Interfaces
- TCP client for chat-like interaction
- Future-proof design for Web UI

### Tech Stack
- Python 3.11+
- `asyncio` for async TCP server
- `aiohttp` for API requests
- `APScheduler` for background alerts
- `SQLite` for watchlist storage
- Docker-ready for deployment

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/market-radar-ai.git
cd market-radar-ai
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the Server:
```
python app/server.py
```

4. Run the TCP client (in another terminal):
```
python client/tcp_client.py
```

### Disclaimer

This project is for educational purposes only. It does not provide financial advice. Stock prices are retrieved from free public APIs and may be delayed.

### Contribution

Contributions welcome! Fork, create issues, and send pull requests.
Designed to be modular and scalable.