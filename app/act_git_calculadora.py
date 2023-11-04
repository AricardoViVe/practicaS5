class Calculadora:
    """Clase dummy sobre una calculadora"""

    def __init__(self) -> None:
        return

    def suma(self, a: float, b: float) -> float:
        """Función transforma dos valores y los suma aritméticamente

        Args :
          a: float:
          b: float:
        Returns: float

        Returns :
            float
        >>> suma('1', 2.0)
        3.0
        Raises :
            TypeError - Levanta una excepción sobre el tipo
        """
        try:
            # El usuario puede ingresar valores tipo int,str,float
            return float(a) + float(b)
        except TypeError:
            print("El número debe tener formato str, int o float")

