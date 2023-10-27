from calculadora import Calculadora
import pytest
calc = Calculadora()

#Prueba Suma
def obtener_datos_suma():
    return [(1,1,2.0),('1','2',3.0),(2.0,'1',3.0)]
@pytest.mark.parametrize('a','b','esperado',obtener_datos_suma())
def test_suma_parametrize(a,b,esperado):
    assert calc.suma(a,b) == esperado
from app.calculadora import Calculadora
import pytest
calc = Calculadora()
calc.suma(1+1)

#Prueba Resta
def obtener_datos_test_resta():
    return[(2,1,1.0), (2,1.0,1.0), ("2", 1.0,1.0), (2, "1.0",1.0), (2.0, 1.0,1.0), ('2-1',None ,1.0)]
@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_resta)
def test_resta_parametrize(a, b,esperado):
    assert calc.resta(a, b) == esperado

#Prueba Multiplicación
def obtener_datos_test_multiplicacion():
    return[(1,2,2.0), (1,2.0,2.0), ("1", 2.0,2.0), (1, "2.0",2.0), (2.0, 1.0,2.0), ('2*1',None ,2.0)]
@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_multiplicacion)
def test_multi_parametrize(a, b,esperado):
    assert calc.multiplicacion(a, b) == esperado

#Prueba División
def obtener_datos_test_division():
    return[(2,1,2.0), (2,1.0,2.0), ("2", 1.0,2.0), (2, "1.0",2.0), (2.0, 1.0,2.0), ('2/1',None ,2.0), (2,0,ValueError)]
@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_division)
def test_division_parametrize(a, b,esperado):
    assert calc.division(a, b) == esperado