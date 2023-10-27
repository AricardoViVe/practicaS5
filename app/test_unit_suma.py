from calculadora import Calculadora
import pytest
calc = Calculadora()
def obtener_datos_suma():
    return [(1,1,2.0),('1','2',3.0),(2.0,'1',3.0)]
@pytest.mark.parametrize('a','b','esperado',obtener_datos_suma())
def test_suma_parametrize(a,b,esperado):
    assert calc.suma(a,b) == esperado
