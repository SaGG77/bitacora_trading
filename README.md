# TradeMorfosis — Journal de Trading

App Flask para llevar una bitácora de trading con interfaz centrada en una sola vista (`journal.html`) + parciales reutilizables.

## Estructura

- `app/templates/journal.html`
- `app/templates/partials/summary_cards.html`
- `app/templates/partials/trade_filters.html`
- `app/templates/partials/trade_table.html`
- `app/templates/partials/trade_form_modal.html`
- `app/templates/partials/trade_detail_modal.html`

## Funcionalidad

- Resumen superior: Profit total, Win rate, Trades totales, Mejor activo, Peor emoción y Profit del mes.
- Filtros en cliente: fecha, activo, dirección, emoción y tipo de entrada.
- Tabla principal de trades.
- Botón **Nuevo trade** que abre modal.
- Modal de detalle para comentario y captura.

## Ejecutar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abrir: `http://127.0.0.1:5000`
