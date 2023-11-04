import pytest
from app.calculadora import Calculadora
import sys
sys.path.append("/Users/rich/Documents/DiploMLops/20102023/practica_uno/Integra/practicaS5/app/")  # noqa: E501


# Prueba Suma
def obtener_datos_suma():
    return [(1, 1, 2.0), ("1", "2", 3.0), (2.0, "1", 3.0)]


@pytest.mark.parametrize("a, b, esperado", obtener_datos_suma())
def test_suma_parametrize(a, b, esperado):
    calc = Calculadora()
    resultado = calc.suma(a, b)
    assert resultado == esperado


# Prueba Resta
def obtener_datos_test_resta():
    return [
        (2, 1, 1.0),
        (2, 1.0, 1.0),
        ("2", 1.0, 1.0),
        (2, "1.0", 1.0),
        (2.0, 1.0, 1.0),
    ]


@pytest.mark.parametrize("a, b, esperado", obtener_datos_test_resta())
def test_resta_parametrize(a, b, esperado):
    calc = Calculadora()
    resultado = calc.resta(a, b)
    assert resultado == esperado


# Prueba Multiplicación
def obtener_datos_test_multiplicacion():
    return [
        (1, 2, 2.0),
        (1, 2.0, 2.0),
        ("1", 2.0, 2.0),
        (1, "2.0", 2.0),
        (2.0, 1.0, 2.0),
    ]


@pytest.mark.parametrize("a, b, esperado", obtener_datos_test_multiplicacion())
def test_multi_parametrize(a, b, esperado):
    calc = Calculadora()
    resultado = calc.multiplicacion(a, b)
    assert resultado == esperado

# Prueba Potencia


def obtener_datos_test_potencia():
    return [
        (2/3, 3/1, 0.2962962962962962),
        (-3/2, 2.25, "no permitido, raiz de un numero negativo"),
        (3/2, 2/2, 3/2),
        (2, 3/2, 2.8284271247461903),
    ]


@pytest.mark.parametrize("a, b, esperado", obtener_datos_test_potencia())
def test_potencia_parametrize(a, b, esperado):
    calc = Calculadora()
    resultado = calc.potencia_raiz(a, b)
    assert resultado == esperado


# Prueba División
def obtener_datos_test_division():
    return [
        (2, 1, 2.0),
        (2, 1.0, 2.0),
        ("2", 1.0, 2.0),
        (2, "1.0", 2.0),
        (2.0, 1.0, 2.0),
        (2, 0, 'Division entre cero')
    ]


@pytest.mark.parametrize("a, b, esperado", obtener_datos_test_division())
def test_division_parametrize(a, b, esperado):
    calc = Calculadora()
    resultado = calc.division(a, b)
    assert resultado == esperado


# Prueba operaciones string
def obtener_datos_test_strings():
    return [
        (2, 1, "*", 2.0),
        (2, 1.0, "+", 3.0),
        (2.0, 1.0, "/", 2.0),
        (2.0, 1.0, "-", 1.0),
    ]


@pytest.mark.parametrize("a, b, c, esperado", obtener_datos_test_strings())
def test_strings_parametrize(a, b, c, esperado):
    calc = Calculadora()
    resultado = calc.do_operation(a, b, c)
    assert resultado == esperado
