def technical_score(price: float, sma_20: float | None, sma_50: float | None, rsi_value: float | None):
    score = 0
    reasons = []

    if sma_20 and price > sma_20:
        score += 1
        reasons.append("Price above 20-day SMA")

    if sma_50 and price > sma_50:
        score += 1
        reasons.append("Price above 50-day SMA")

    if rsi_value:
        if rsi_value < 30:
            score += 2
            reasons.append("RSI indicates oversold")
        elif rsi_value > 70:
            score -= 2
            reasons.append("RSI indicates overbought")

    if score >= 3:
        recommendation = "BUY"
    elif score >= 1:
        recommendation = "HOLD"
    else:
        recommendation = "WAIT"

    return recommendation, score, reasons
