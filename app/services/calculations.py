def classify_result(resultado_dinero: float | None) -> str:
    if resultado_dinero is None:
        return "breakeven"
    if resultado_dinero > 0:
        return "win"
    if resultado_dinero < 0:
        return "loss"
    return "breakeven"
