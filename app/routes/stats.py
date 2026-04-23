from flask import Blueprint, render_template

from app.models import Trade
from app.services import build_summary

stats_bp = Blueprint("stats", __name__)


@stats_bp.get("/")
def stats():
    trades = Trade.query.order_by(Trade.fecha.desc(), Trade.hora.desc()).all()
    summary = build_summary(trades)
    return render_template("stats.html", summary=summary)
