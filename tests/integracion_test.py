import sys 
sys.path.append('/Users/rich/Documents/DiploMLops/20102023/practica_uno/Integra/practicaS5/app')  
#sys.path.append("C:\\Users\\Andrew S\\Documents\\Trabajo\\Diplomado MLOps\\practicaS5\\app")  


from app.calculadora import Calculadora
import pytest

def datos_integracion():
  return [
     ("(5+5)*(1.25-0.75)", 5),
     ("(8+7/5)*(15-3/8)", 137.475)
     ]

@pytest.mark.parametrize('operacion, esperado', datos_integracion())
def test_operacion_parametrize(operacion, esperado):
  calc = Calculadora()  
  resultado = calc.input(operacion) 
  assert resultado == esperado

# Pruebas con funciones anidadas
def obtener_datos_test_calc_anidada():
    return[
        (5, 5, 1.25, -0.75, 5),
        (8, 7/5, 15, -3/8, 137.475)
    ]
@pytest.mark.parametrize("a, b, c, d, esperado", obtener_datos_test_calc_anidada())
def test_cal_anidada(a,b,c,d, esperado):
    calc = Calculadora()
    resultado = calc.multiplicacion(calc.suma(a,b), calc.suma(c,d))
    assert resultado == esperado

  # Pruebas con funciones anidadas, pasando como parámetro el operador
def obtener_datos_test_calc_anidada_op():
    return[
        (5, 5, 1.25, -0.75, 5),
        (8, 7/5, 15, -3/8, 137.475)
    ]
@pytest.mark.parametrize("a, b, c, d, esperado", obtener_datos_test_calc_anidada_op())
def test_cal_anidada(a,b,c,d, esperado):
    calc = Calculadora()
    operacion = calc.do_operation(calc.do_operation(a,b, "+"), calc.do_operation(c, d, "+"),"*")
    assert operacion == esperado

