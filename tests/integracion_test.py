
import pytest
from app.calculadora import Calculadora
import sys
sys.path.append("/Users/rich/Documents/DiploMLops/20102023/practica_uno/Integra/practicaS5/app/")  # noqa: E501


def datos_integracion():
    return [("(5+5)*(1.25-0.75)*(0.5)^(0.25)", 4.20448207626857),
            ("(8+7/5)*(15-3/8)*(8/2)^(1/2)", 274.95)]


@pytest.mark.parametrize("operacion, esperado", datos_integracion())
def test_operacion_parametrize(operacion, esperado):
    calc = Calculadora()
    resultado = calc.input(operacion)
    assert resultado == esperado


# Pruebas con funciones anidadas
def obtener_datos_test_calc_anidada():
    return [(5, 5, 1.25, -0.75, 0.5, 0.25, 4.20448207626857),
            (8, 7 / 5, 15, -3 / 8, 8 / 2, 1 / 2, 274.95)]


@pytest.mark.parametrize("a, b, c, d, e, f, esperado", obtener_datos_test_calc_anidada())  # noqa: E501
def test_cal_anidada(a, b, c, d, e, f, esperado):
    calc = Calculadora()
    resultado = calc.multiplicacion(
        calc.suma(a, b), calc.suma(c, d), calc.potencia(e, f))
    assert resultado == esperado
