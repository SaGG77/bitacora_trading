from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, NumberRange, Optional


class TradeForm(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired()])
    hora = TimeField("Hora", validators=[DataRequired()])
    activo = StringField("Activo", validators=[DataRequired()])
    direccion = SelectField("Dirección", choices=[("Buy", "Buy"), ("Sell", "Sell")], validators=[DataRequired()])
    tipo_entrada = SelectField(
        "Tipo de entrada",
        choices=[("Rompimiento", "Rompimiento"), ("Retroceso", "Retroceso"), ("Anticipado", "Anticipado")],
        validators=[DataRequired()],
    )
    lotaje = FloatField("Lotaje", validators=[DataRequired(), NumberRange(min=0.01)])
    entrada = FloatField("Entrada", validators=[DataRequired()])
    stop_loss = FloatField("Stop Loss", validators=[Optional()])
    take_profit = FloatField("Take Profit", validators=[Optional()])
    salida = FloatField("Salida", validators=[Optional()])
    resultado_pips = FloatField("Resultado pips", validators=[Optional()])
    resultado_dinero = FloatField("Resultado USD", validators=[Optional()])
    emocion = StringField("Emoción", validators=[Optional()])
    comentario = TextAreaField("Comentario", validators=[Optional()])
    captura = StringField("Captura (URL)", validators=[Optional()])
    submit = SubmitField("Guardar trade")
