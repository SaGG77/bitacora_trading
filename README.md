# Tradeando 📈

Bitácora de trading construida con **Flask + Bootstrap + JavaScript**, usando **SQLAlchemy** para persistencia.

## Características

- Dashboard con métricas clave (total de trades, ganadas, perdidas y win rate).
- Tabla completa de operaciones con todos los datos de tu hoja.
- Filtro instantáneo por activo (JS).
- Estilo limpio y entendible para revisar tu desempeño rápidamente.

## Stack

- Flask
- Flask-SQLAlchemy
- Bootstrap 5
- JavaScript vanilla
- SQLite

## Ejecutar en local

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Luego abre: `http://127.0.0.1:5000`

La base de datos (`bitacora.db`) se crea automáticamente con datos iniciales.
