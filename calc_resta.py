"""Module providing a function for command line parameters."""
import sys

def resta(n1, n2):
    """

    Args:
      n1: Número al que se le restara el segundo parámetro
      n2: Número que se restará al prmier parámetro

    Returns: la diferencia de num1 y num2

    """
    return n1 - n2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: calc.py <num1> <num2>")
    else:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = resta(num1, num2)
            print(f"la resta de  {num1} y {num2} es: {result}")
        except ValueError:
            print("Por favor ingresa valores validos.")
