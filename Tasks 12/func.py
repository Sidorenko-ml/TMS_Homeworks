# Программа должна содержать 4 функции принимающие два аргумента и возвращающие результаты 
#  сложения, вычитания, умножения и деления.
class Calc:
    """Калькулятор"""
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def summ(self):
        return (self.a + self.b)
    
    def sub(self):
        return (self.a - self.b)
    
    def div(self):
        if self.b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        else:
            return (self.a / self.b)
    
    def mul(self):
        return (self.a * self.b)