from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    trades = db.relationship("Trade", backref="user", lazy=True)
