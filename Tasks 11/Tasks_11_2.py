# Создать статичный метод get_random_name для класса Pet. Метод возвращает случайную строку вида A-42
import random

class Pet():
    """ Так же пустой класс для создания статичного метода get_random_name """

    def __init__(self) -> None:
       pass 
    
    @staticmethod
    def get_random_name():
        str1 = '0123456789'
        str2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        name = random.choice(str2) + '-' + random.choice(str1) + random.choice(str1)
        print(name)
        return name
    
Pet.get_random_name()