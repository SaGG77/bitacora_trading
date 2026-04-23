from flask import Blueprint, redirect, request, url_for

from app.extensions import db
from app.forms import TradeForm
from app.models import Trade, User

trades_bp = Blueprint("trades", __name__)


@trades_bp.post("/save")
def save_trade():
    trade_id = request.form.get("trade_id")
    form = TradeForm()
    if not form.validate_on_submit():
        return redirect(url_for("main.journal"))

    if trade_id:
        trade = Trade.query.get_or_404(trade_id)
        form.populate_obj(trade)
    else:
        user = User.query.first()
        trade = Trade(user_id=user.id)
        form.populate_obj(trade)
        db.session.add(trade)

    trade.activo = trade.activo.upper()
    db.session.commit()
    return redirect(url_for("main.journal"))


@trades_bp.post("/<int:trade_id>/delete")
def delete_trade(trade_id: int):
    trade = Trade.query.get_or_404(trade_id)
    db.session.delete(trade)
    db.session.commit()
    return redirect(url_for("main.journal"))
