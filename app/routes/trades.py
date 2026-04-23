import csv
from datetime import datetime
from io import StringIO

from flask import Blueprint, Response, flash, redirect, request, url_for

from app.extensions import db
from app.forms import TradeForm
from app.models import Trade, User

trades_bp = Blueprint("trades", __name__)


@trades_bp.post("/save")
def save_trade():
    trade_id = request.form.get("trade_id")
    form = TradeForm()
    if not form.validate_on_submit():
        flash("Revisa los campos del formulario antes de guardar.", "warning")
        return redirect(url_for("main.journal"))

    if trade_id:
        trade = Trade.query.get_or_404(trade_id)
        form.populate_obj(trade)
    else:
        user = User.query.first()
        if not user:
            flash("No existe usuario base para crear operaciones.", "danger")
            return redirect(url_for("main.journal"))
        trade = Trade(user_id=user.id)
        form.populate_obj(trade)
        db.session.add(trade)

    trade.activo = trade.activo.upper()
    db.session.commit()
    flash("Trade guardado correctamente.", "success")
    return redirect(url_for("main.journal"))


@trades_bp.post("/<int:trade_id>/delete")
def delete_trade(trade_id: int):
    trade = Trade.query.get_or_404(trade_id)
    db.session.delete(trade)
    db.session.commit()
    flash("Trade eliminado.", "info")
    return redirect(url_for("main.journal"))


@trades_bp.get("/export.csv")
def export_csv():
    filters = {
        "fecha_desde": request.args.get("fecha_desde", "").strip(),
        "fecha_hasta": request.args.get("fecha_hasta", "").strip(),
        "activo": request.args.get("activo", "").strip(),
        "direccion": request.args.get("direccion", "").strip(),
        "emocion": request.args.get("emocion", "").strip(),
        "tipo_entrada": request.args.get("tipo_entrada", "").strip(),
    }

    query = Trade.query
    if filters["fecha_desde"]:
        try:
            query = query.filter(Trade.fecha >= datetime.strptime(filters["fecha_desde"], "%Y-%m-%d").date())
        except ValueError:
            pass
    if filters["fecha_hasta"]:
        try:
            query = query.filter(Trade.fecha <= datetime.strptime(filters["fecha_hasta"], "%Y-%m-%d").date())
        except ValueError:
            pass
    if filters["activo"]:
        query = query.filter(Trade.activo.ilike(f"%{filters['activo']}%"))
    if filters["direccion"]:
        query = query.filter(Trade.direccion == filters["direccion"])
    if filters["emocion"]:
        query = query.filter(Trade.emocion.ilike(f"%{filters['emocion']}%"))
    if filters["tipo_entrada"]:
        query = query.filter(Trade.tipo_entrada.ilike(f"%{filters['tipo_entrada']}%"))

    trades = query.order_by(Trade.fecha.desc(), Trade.hora.desc()).all()

    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["fecha", "hora", "activo", "direccion", "tipo_entrada", "resultado_pips", "resultado_usd", "emocion", "comentario"])
    for t in trades:
        writer.writerow([t.fecha, t.hora.strftime("%H:%M"), t.activo, t.direccion, t.tipo_entrada, t.resultado_pips, t.resultado_dinero, t.emocion, t.comentario])

    return Response(
        buffer.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=trading_journal.csv"},
    )
