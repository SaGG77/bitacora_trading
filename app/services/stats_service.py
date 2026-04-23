from collections import Counter, defaultdict
from datetime import date

from .calculations import classify_result


def build_summary(trades):
    total = len(trades)
    wins = sum(1 for t in trades if classify_result(t.resultado_dinero) == "win")
    profit_total = sum((t.resultado_dinero or 0) for t in trades)

    monthly_profit = sum(
        (t.resultado_dinero or 0)
        for t in trades
        if t.fecha.month == date.today().month and t.fecha.year == date.today().year
    )

    by_asset = defaultdict(float)
    emotions = Counter()
    for t in trades:
        by_asset[t.activo] += t.resultado_dinero or 0
        if t.emocion:
            emotions[t.emocion] += 1

    best_asset = max(by_asset, key=by_asset.get) if by_asset else "-"
    worst_emotion = emotions.most_common(1)[0][0] if emotions else "-"

    return {
        "profit_total": round(profit_total, 2),
        "win_rate": round((wins / total * 100), 2) if total else 0,
        "total_trades": total,
        "best_asset": best_asset,
        "worst_emotion": worst_emotion,
        "monthly_profit": round(monthly_profit, 2),
    }
