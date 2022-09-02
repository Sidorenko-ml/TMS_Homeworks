# Создать класс MyTime. Атрибуты: hours, minutes, seconds. 
# Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >), сложения, вычитания, умножения на число, вывод на экран. 
# Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/

class MyTime:
    __daySeconds = 86400
    s = None
    m = None
    h = None
    def __init__(self, seconds:int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть типом int')
        self.seconds = seconds % self.__daySeconds

    def get_time(self):
        self.s = self.seconds % 60
        self.m = self.seconds // 60 % 60
        self.h = self.seconds // 3600 % 24
        return f'{self.__get_formatted(self.h)}:{self.__get_formatted(self.m)}:{self.__get_formatted(self.s)}'

    @classmethod
    def __get_formatted(cls,x):
        return str(x).rjust(2, '0')
    
    def __eq__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc 
    
    def __le__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc
    
    def __ge__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds >= sc
    
    def __lt__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc
    
    def __gt__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds > sc
    def __add__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return MyTime(self.seconds + sc)
    
    def __sub__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return MyTime(self.seconds - sc)
    
    def __mul__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, int) else other.seconds
        return MyTime(self.seconds * sc)

    def __truediv__(self,other):
        if not isinstance(other, (int, MyTime)):
            raise TypeError("Неверный формат")
        sc = other if isinstance(other, (int,float)) else other.seconds
        return MyTime(self.seconds // sc)
    
    def __str__(self):
        return f'Время в данный момент - {self.get_time()}'