from datetime import date, datetime, time
from pathlib import Path

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "bitacora.db"

db = SQLAlchemy()


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    activo = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(10), nullable=False)
    lotaje = db.Column(db.Float, nullable=False)
    entrada = db.Column(db.Float, nullable=False)
    tp = db.Column(db.Float, nullable=False)
    sl = db.Column(db.Float, nullable=False)
    salida = db.Column(db.Float, nullable=False)
    pips = db.Column(db.Float, nullable=False)
    resultado_usd = db.Column(db.Float, nullable=False)
    riesgo_r = db.Column(db.Float, nullable=False)
    error_plan = db.Column(db.Integer, nullable=False, default=0)
    pnl_mostrar = db.Column(db.String(20), nullable=False)
    emocion = db.Column(db.String(20), nullable=False)
    setup = db.Column(db.String(50), nullable=False)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        trades = Trade.query.order_by(Trade.fecha.desc(), Trade.hora.desc()).all()
        total_trades = len(trades)
        ganadas = sum(1 for t in trades if t.resultado_usd > 0)
        perdidas = total_trades - ganadas
        neto = sum(t.resultado_usd for t in trades)
        win_rate = (ganadas / total_trades * 100) if total_trades else 0

        return render_template(
            "index.html",
            app_name="TradeMorfosis",
            trades=trades,
            stats={
                "total": total_trades,
                "ganadas": ganadas,
                "perdidas": perdidas,
                "neto": neto,
                "win_rate": win_rate,
            },
        )

    with app.app_context():
        db.create_all()
        seed_data()

    return app


def seed_data() -> None:
    if Trade.query.count() > 0:
        return

    muestras = [
        {
            "fecha": date(2025, 6, 20),
            "hora": time(9, 0),
            "activo": "XAUUSD",
            "direccion": "Buy",
            "lotaje": 0.5,
            "entrada": 2310,
            "tp": 2318,
            "sl": 2300,
            "salida": 2320,
            "pips": 80,
            "resultado_usd": 400,
            "riesgo_r": -2,
            "error_plan": 0,
            "pnl_mostrar": "$398,00",
            "emocion": "Confiado",
            "setup": "Rompimiento",
        },
        {
            "fecha": date(2025, 6, 21),
            "hora": time(14, 0),
            "activo": "BTCUSD",
            "direccion": "Sell",
            "lotaje": 0.1,
            "entrada": 65000,
            "tp": 64000,
            "sl": 66000,
            "salida": 64000,
            "pips": 1000,
            "resultado_usd": 100,
            "riesgo_r": -1.5,
            "error_plan": 0,
            "pnl_mostrar": "$98,50",
            "emocion": "Neutral",
            "setup": "Retroceso",
        },
        {
            "fecha": date(2025, 6, 22),
            "hora": time(10, 30),
            "activo": "EURUSD",
            "direccion": "Buy",
            "lotaje": 1,
            "entrada": 1.070,
            "tp": 1.065,
            "sl": 1.068,
            "salida": 1.075,
            "pips": -50,
            "resultado_usd": -500,
            "riesgo_r": -3,
            "error_plan": 0,
            "pnl_mostrar": "-$503,00",
            "emocion": "Ansioso",
            "setup": "Anticipado",
        },
    ]

    db.session.add_all(Trade(**dato) for dato in muestras)
    db.session.commit()


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
