# Создать метод класса get_counter. Создать три объекта класса. Вызвать через класс метод get_counter.

class First():
    """Пустой класс для создания метода get_counter"""

    def __init__(self) -> None:
        print("Экземпляр класса создан")
    
    def get_counter(self):
        print("Вызван метод get_counter")

x = First()
x2 = First()
x3 = First()

x3.get_counter()