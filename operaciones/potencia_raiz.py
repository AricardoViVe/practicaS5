from utils.fracciones import obtener_fracciones

def potencia(a, b):
    """eleva una fraccion a una potencia en fraccion"""
    base = obtener_fracciones(a)
    potencia = obtener_fracciones(b)
    comprobacion=potencia-int(potencia)
    
    if (base < 0) & (comprobacion!=0):
        return "no permitido, raiz de un numero negativo"
    else:
        return (base) ** (potencia)