# Сделать класс Pet абстрактным
from abc import ABC, abstractmethod

class Pet(ABC):
    @abstractmethod
    def invisible1(self):
        print("Я должен быть невидим для остальных")
    
    def invisible2(self):
        print("А тут по идее видим")

class Pet2(Pet):
    pass

x = Pet2()
x.invisible2()