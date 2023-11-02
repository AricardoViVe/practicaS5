from utils.fracciones import obtener_fracciones

def potencia(a, b):
    """eleva una fraccion a una potencia en fraccion"""
    base = obtener_fracciones(a)
    potencia = obtener_fracciones(b)
    
    return base ** potencia
