import sys 
# sys.path.append('/Users/rich/Documents/DiploMLops/20102023/practica_uno/Integra/practicaS5/app')  
sys.path.append("C:\\Users\\Andrew S\\Documents\\Trabajo\\Diplomado MLOps\\practicaS5\\app")  


from app.calculadora import Calculadora
import pytest

def datos_integracion():
  return [("(5+5)*(1.25-0.75)", 5),("(8+7/5)*(15-3/8)", 137.475)]

@pytest.mark.parametrize('operacion, esperado', datos_integracion())
def test_operacion_parametrize(operacion, esperado):
  calc = Calculadora()  
  resultado = calc.input(operacion) 
  assert resultado == esperado


#Prueba Resta
def obtener_datos_test_resta():
    return[(2,1,1.0), (2,1.0,1.0), ("2", 1.0,1.0), (2, "1.0",1.0), (2.0, 1.0,1.0), ('2-1',None ,1.0)]
@pytest.mark.parametrize('a, b, esperado', obtener_datos_test_resta())
def test_resta_parametrize(a, b,esperado):
  calc = Calculadora()  
  resultado = calc.resta(a,b) 
  assert calc.resta(a, b) == esperado