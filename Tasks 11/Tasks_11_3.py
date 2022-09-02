# Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в классах методы voice.
# Создать класс Mule. Метод voice должен быть унаследован от класса Donkey

import random

class Pet():
    """ Класс-родитель """
    def __init__(self):
       pass 
    
    def voice(self):
        print('Pet издает звук')

class Horse(Pet):
    def __init__(self):
       pass

    def voice(self):
        print('Horse издает звук')

class Donkey(Pet):
    def __init__(self):
       pass
    
    def voice(self):
        print('Donkey издает звук')

class Mule(Donkey):
    def __init__(self):
       pass

x1 = Mule()
x1.voice()
