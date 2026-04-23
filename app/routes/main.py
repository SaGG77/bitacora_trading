from datetime import datetime

from flask import Blueprint, render_template, request

from app.forms import TradeForm
from app.models import Trade
from app.services import build_summary

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def journal():
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
            desde = datetime.strptime(filters["fecha_desde"], "%Y-%m-%d").date()
            query = query.filter(Trade.fecha >= desde)
        except ValueError:
            pass
    if filters["fecha_hasta"]:
        try:
            hasta = datetime.strptime(filters["fecha_hasta"], "%Y-%m-%d").date()
            query = query.filter(Trade.fecha <= hasta)
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
    summary = build_summary(trades)
    form = TradeForm()
    return render_template("journal.html", trades=trades, summary=summary, form=form, filters=filters)
