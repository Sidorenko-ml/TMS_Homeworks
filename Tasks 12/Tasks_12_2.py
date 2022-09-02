# Создать класс Point, описывающий точку(атрибуты: x, y). 
# Создать класс Figure. Создать три дочерних класса: 
# Circle(атрибуты: координаты центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности), 
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра), 
# Square(атрибуты: размер стороны, методы: нахождение площади и периметра). 
# При потребности создавать все необходимые методы не описанные в задании. 
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
# Примечание: в рамках задание создать два файла: Tasks12_2.py и Tasks12_3.py. 
# В первом будут описаны все классы, во втором классы будут импортированы и использованы.

class Point:
    """Класс описывающий точку, содержит координаты x и y"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Figure:
    '''Класс описывающий геометрическую фигуру, содержит вывод данных - Площадь и Периметр'''
    def __init__(self, s= 0, p=0):
        self.s = s
        self.p = p
    def print_info(self):
        print(f'S = {self.s}')
        print(f'P = {self.p}')

class Circle(Figure):
    Pi = 3.1415
    def __init__(self,r,x = 0, y = 0):
        self.x = x
        self.y = y
        self.r = r
    def perimeter(self):
        p = 2 * self.Pi * int(self.r)
        return p
    def square(self):
        s = self.Pi * (self.r ** 2)
        return s
    def __str__(self):
        return f'Периметр окружности равен = {self.perimeter()}\nПлощадь окружности равна = {self.square()}'

class Triangle(Figure):
    def __init__(self, a , b , c):
        self.a = a
        self.b = b
        self.c = c
    def perimetr(self,p = None):
        p = self.a + self.b + self.c
        return p
    def square(self):
        pp = (self.a + self.b + self.c) / 2
        h = (2 * ((pp*(pp-self.a)*(pp-self.b)*(pp-self.c))**0.5)) / self.a
        s = 0.5 * self.a * h
        return s
    def __str__(self):
        return f'Периметр треугольника равен = {self.perimetr()}\nПлощадь треугольника равна = {self.square()}'

class Square(Figure):
    def __init__(self, a):
        self.a = a
    def perimetr(self):
        p = 4 * self.a 
        return p
    def square(self):
        s = self.a ** 2
        return s
    def __str__(self):
        return f'Периметр квадрата равен = {self.perimetr()}\nПлощадь квадрата равна = {self.square()}'
