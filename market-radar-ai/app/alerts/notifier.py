"""
Alert Notifier.

Handles alert delivery.
(Currently console-based.)
"""


def send_alert(symbol: str, price: float, target: float) -> None:
    """
    Send stock alert.
    """
    print(
        f"🚨 BUY ALERT: {symbol}\n"
        f"Current Price: ₹{price}\n"
        f"Target Price: ₹{target}\n"
    )
