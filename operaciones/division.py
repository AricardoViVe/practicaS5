from utils.fracciones import obtener_fracciones


def division(a, b):
    """Divide dos fracciones."""
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"
