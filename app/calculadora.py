from operaciones.division import division
from operaciones.multiplicacion import multi
from operaciones.resta import resta
from operaciones.suma import suma
from operaciones.potencia_raiz import potencia


class Calculadora:
    """Objeto que simula una calculadora"""

    def __init__(self):
        pass

    def find_operator(self, s, op):
        return s.find(op)

    def find_tokens(self, s, op):
        open_parenthesis = s.rfind("(")
        close_parenthesis = s.find(")", open_parenthesis)
        operator_index = s.find(op, open_parenthesis, close_parenthesis)
        tokens = [
            s[open_parenthesis + 1:operator_index],
            s[operator_index + 1:close_parenthesis],
        ]
        return tokens

    def get_operands(self, s, op):
        op_index = s.index(op)
        a = s[:op_index]
        b = s[op_index + 1:]
        if self.find_operator(a, "/") != -1:
            a = str(int(a[0]) / (int(a[-1])))
        else:
            a
        if self.find_operator(b, "/") != -1:
            b = str(int(b[0]) / (int(b[-1])))
        else:
            b
        return a, b

    def get_operation(self, s, op):
        a, b = self.get_operands(s, op)
        if op == "+":
            return self.suma(float(a), float(b))
        elif op == "-":
            return self.resta(float(a), float(b))
        elif op == "*":
            return self.multiplicacion(float(a), float(b))
        elif op == "^":
            return self.potencia_raiz(float(a), float(b))

    def get_operation_for_token(self, token):
        if self.find_operator(token, "+") != -1:
            return self.get_operation(token, "+")
        elif self.find_operator(token, "-") != -1:
            return self.get_operation(token, "-")
        elif self.find_operator(token, "*") != -1:
            return self.get_operation(token, "*")
        elif self.find_operator(token, "^") != -1:
            return self.get_operation(token, "^")

    def do_operation(self, a, b, op):
        if op == "+":
            return self.suma(a, b)
        elif op == "-":
            return self.resta(a, b)
        elif op == "*":
            return self.multiplicacion(a, b)
        elif op == "/":
            return self.division(a, b)
        elif op == "^":
            return self.potencia_raiz(a, b)

    def calculate(self, s):
        s = s.replace(" ", "")
        while "(" in s:
            open_parenthesis = s.rfind("(")
            close_parenthesis = s.find(")", open_parenthesis)
            token = s[open_parenthesis + 1:close_parenthesis]
            result = self.get_operation_for_token(token)
            s = s[:open_parenthesis] + str(result) + s[close_parenthesis + 1:]
        return float(self.get_operation_for_token(s))

    def input(self, s):
        return self.calculate(s)

    def suma(self, a, b):
        return suma(a, b)

    def resta(self, a, b):
        return resta(a, b)

    def multiplicacion(self, a, b):
        return multi(a, b)

    def division(self, a, b):
        return division(a, b)

    def potencia_raiz(self, a, b):
        return potencia(a, b)
