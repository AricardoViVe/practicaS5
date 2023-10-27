from app.calculadora import Calculadora
import pytest
calc = Calculadora()
calc.suma(1+1)

#Prueba Suma
def obtener_datos_test_suma():
    return[(1,2,3.0), (1,2.0,3.0), ("1", 2.0,3.0), (1, "2.0",3.0), (2.0, 1.0,3.0), ('2+1',None ,3.0)]

@pytest.mark.parametrize('numero1, numero2, esperado', obtener_datos_test_suma)
def test_suma_parametrize(numero1, numero2,esperado):
    assert calc.suma(numero1, numero2) == esperado

#Prueba Resta
def obtener_datos_test_resta():
    return[(2,1,1.0), (2,1.0,1.0), ("2", 1.0,1.0), (2, "1.0",1.0), (2.0, 1.0,1.0), ('2-1',None ,1.0)]

@pytest.mark.parametrize('numero1, numero2, esperado', obtener_datos_test_resta)
def test_resta_parametrize(numero1, numero2,esperado):
    assert calc.resta(numero1, numero2) == esperado

#Prueba Multiplicación
def obtener_datos_test_multiplicacion():
    return[(1,2,2.0), (1,2.0,2.0), ("1", 2.0,2.0), (1, "2.0",2.0), (2.0, 1.0,2.0), ('2*1',None ,2.0)]

@pytest.mark.parametrize('numero1, numero2, esperado', obtener_datos_test_multiplicacion)
def test_multi_parametrize(numero1, numero2,esperado):
    assert calc.multiplicacion(numero1, numero2) == esperado

#Prueba División
def obtener_datos_test_division():
    return[(2,1,2.0), (2,1.0,2.0), ("2", 1.0,2.0), (2, "1.0",2.0), (2.0, 1.0,2.0), ('2/1',None ,2.0), (2,0,ValueError)]

@pytest.mark.parametrize('numero1, numero2, esperado', obtener_datos_test_division)
def test_division_parametrize(numero1, numero2,esperado):
    assert calc.division(numero1, numero2) == esperado