from flask import Blueprint, render_template

from app.forms import TradeForm
from app.models import Trade
from app.services import build_summary

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def journal():
    trades = Trade.query.order_by(Trade.fecha.desc(), Trade.hora.desc()).all()
    summary = build_summary(trades)
    form = TradeForm()
    return render_template("journal.html", trades=trades, summary=summary, form=form)
