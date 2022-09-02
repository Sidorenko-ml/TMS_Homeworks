# Реализовать следующую структуру:
#                 Animal
#     Pet                     WildAnimal
# Cat     Dog                Lion    Wolf

class Animal():
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Animal")


class Pet(Animal):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Pet. Мой родитель Animal. А ещё у меня есть 2 дочки")


class Cat(Pet):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Cat. Мой родитель - Pet")

class Dog(Pet):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Dog. Мой родитель - Pet, а сестра - Cat")

class WildAnimal(Animal):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть WildAnimal. Мой родитель - Animal")

class Lion(WildAnimal):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Lion. Мой родитель - WildAnimal, а брат - Wolf")

class Wolf(WildAnimal):
    def __init__(self) -> None:
        pass
    def I_am(self):
        print("Я есть Wolf. Мой родитель - WildAnimal")
