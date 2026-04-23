from datetime import date, time

from flask import Flask

from config import DevelopmentConfig
from .extensions import db
from .models import Trade, User
from .routes.main import main_bp
from .routes.stats import stats_bp
from .routes.trades import trades_bp


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(trades_bp, url_prefix="/trades")
    app.register_blueprint(stats_bp, url_prefix="/stats")

    with app.app_context():
        db.create_all()
        seed_initial_data()

    return app


def seed_initial_data() -> None:
    user = User.query.first()
    if not user:
        user = User(name="Trader Demo")
        db.session.add(user)
        db.session.flush()

    if Trade.query.count() > 0:
        db.session.commit()
        return

    db.session.add_all(
        [
            Trade(
                fecha=date(2025, 6, 20),
                hora=time(9, 0),
                activo="XAUUSD",
                direccion="Buy",
                tipo_entrada="Rompimiento",
                lotaje=0.5,
                entrada=2310,
                stop_loss=2300,
                take_profit=2318,
                salida=2320,
                resultado_pips=80,
                resultado_dinero=398,
                emocion="Confiado",
                comentario="Ruptura limpia de máximo intradía.",
                captura="",
                user_id=user.id,
            ),
            Trade(
                fecha=date(2025, 6, 21),
                hora=time(14, 0),
                activo="BTCUSD",
                direccion="Sell",
                tipo_entrada="Retroceso",
                lotaje=0.1,
                entrada=65000,
                stop_loss=66000,
                take_profit=64000,
                salida=64000,
                resultado_pips=1000,
                resultado_dinero=98.5,
                emocion="Neutral",
                comentario="Venta tras pullback a resistencia.",
                captura="",
                user_id=user.id,
            ),
            Trade(
                fecha=date(2025, 6, 22),
                hora=time(10, 30),
                activo="EURUSD",
                direccion="Buy",
                tipo_entrada="Anticipado",
                lotaje=1,
                entrada=1.07,
                stop_loss=1.068,
                take_profit=1.065,
                salida=1.075,
                resultado_pips=-50,
                resultado_dinero=-503,
                emocion="Ansioso",
                comentario="Entrada temprana, sin confirmación.",
                captura="",
                user_id=user.id,
            ),
        ]
    )
    db.session.commit()
