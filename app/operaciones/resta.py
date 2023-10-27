from utils.fracciones import obtener_fracciones
def resta(a, b):
    """Resta dos fracciones."""
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo