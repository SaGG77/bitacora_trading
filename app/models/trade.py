from datetime import datetime

from app.extensions import db


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    activo = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(10), nullable=False)
    tipo_entrada = db.Column(db.String(40), nullable=False)
    lotaje = db.Column(db.Float, nullable=False)
    entrada = db.Column(db.Float, nullable=False)
    stop_loss = db.Column(db.Float)
    take_profit = db.Column(db.Float)
    salida = db.Column(db.Float)
    resultado_pips = db.Column(db.Float)
    resultado_dinero = db.Column(db.Float)
    emocion = db.Column(db.String(30))
    comentario = db.Column(db.Text)
    captura = db.Column(db.String(255))
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
