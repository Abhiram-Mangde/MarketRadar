from app.storage.price_repository import get_recent_prices
from app.analysis.indicators import sma, rsi
from app.analysis.decision import technical_score

def analyze_technical(symbol: str) -> dict:
    prices = get_recent_prices(symbol, limit=60)

    if len(prices) < 20:
        return {
            "status": "INSUFFICIENT_DATA",
            "message": "Not enough historical data yet."
        }

    current_price = prices[-1]
    sma_20 = sma(prices, 20)
    sma_50 = sma(prices, 50)
    rsi_value = rsi(prices)

    recommendation, score, reasons = technical_score(
        current_price, sma_20, sma_50, rsi_value
    )

    return {
        "price": current_price,
        "sma_20": sma_20,
        "sma_50": sma_50,
        "rsi": rsi_value,
        "score": score,
        "recommendation": recommendation,
        "reasons": reasons
    }
