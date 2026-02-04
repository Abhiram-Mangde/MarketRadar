"""
Alert Scheduler.

Periodically checks watchlist
and evaluates alerts.
"""

import time

from app.alerts.watchlist import init_watchlist, get_watchlist
from app.alerts.alert_engine import evaluate_alerts


def run_scheduler(interval: int = 60) -> None:
    """
    Run alert scheduler loop.

    Args:
        interval (int): Polling interval in seconds
    """
    init_watchlist()

    while True:
        watchlist = get_watchlist()
        alerts = evaluate_alerts(watchlist)

        for alert in alerts:
            print(alert)

        time.sleep(interval)
