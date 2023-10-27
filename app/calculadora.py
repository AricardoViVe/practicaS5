from operaciones.division import division
from operaciones.multiplicacion import multi
from operaciones.resta import resta
from operaciones.suma import suma

class Calculadora:
    """ Objeto que simula una calculadora """
    def __init__(self) -> None:
        pass
    def find_operator(self,s:str,op:str)->bool:
        return s.find(op)
    def find_tokens(self,s:str,op:str)->list:
        opeator_index = s.index(op, s.index(')'),s.index('('))
        tokens = [s[:opeator_index],s[opeator_index:]]
        return tokens
    def get_operands(self,s:str,op:str):
        op_index = s.index(op)
        a = s[:op_index]
        b = s[op_index:]
        return a,b
    def get_operation(self,s:str,op:str):
        if op == '+':
            return self.suma(self.get_operands(s,op))
        elif op == '-':
            return self.resta(self.get_operands(s,op))
        elif op in ('*'):
            return self.multiplicacion(self.get_operands(s,op))
        elif op in ('/'):
            return self.division(self.get_operands(s,op))
        
    def get_operation_for_token(self,token:str):
        if self.find_operator(token,'+'):
            res = self.get_operation(s[1:-1],'+')
        elif self.find_operator(token,'-'):
            res = self.get_operation(s[1:-1],'-')
        elif self.find_operator(token,'*'):
            res = self.get_operation(s[1:-1],'*')
        elif self.find_operator(token,'/'):
            res = self.get_operation(s[1:-1],'+')
        return res
    def do_operation(self,a:float,b:float,op:str):
        if op == '+':
            return self.suma(a,b)
        elif op == '-':
            return self.resta(a,b)
        elif op == '*':
            return self.multiplicacion(a,b)
        elif op == '/':
            return self.division(a,b)


    def input(self,s:str,b:float=None,operation:str=None):
        if b==None:
            s = s.replace(' ','')
            if self.find_operator(s,')') or self.find_operator(s,'('):
                tokens = self.find_tokens(s=s,op='*')
                results =[]
                for token in tokens:
                    results.append(self.get_operation_for_token(token=token))
                final_result = self.multiplicacion(results[0],results[1])
            else:
                final_result=self.get_operation_for_token(s)
            return final_result
        else:
            self.do_operation(a,b,operation)

    def suma(self, a: float, b: float) -> float:
        return suma(a,b)
    def resta(self, a:float, b:float)->float:
        return resta(a,b)
    def multiplicacion(self,a:float,b:float)->float:
        return multi(a,b)
    def division(self,a:float,b:float)->float:
        return division(a,b)
    

