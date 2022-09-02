# Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0). 
# Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), 
# стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, brand, model, years_of_release, speed = 0):        
        self.__brand = brand
        self.__model = model
        self.__year_of_release = years_of_release
        self.__speed = speed

    def print_public_info(self):
        print(f"Ваша машина {self.__brand} {self.__model}, {self.__year_of_release} года выпуска движется со скоростью {self.__speed} км/ч")

    def speed_increase(self):
        self.__speed += 5
        print('Текущая скорость равна - ',self.__speed)

    def reduce_the_speed(self):
        self.__speed -= 5
        print("Текущая скорость равна - ", self.__speed)

    def stop_car(self):
        self.__speed = 0
        print("Текущая скорость равна - ", self.__speed)
    
    def print_speed(self):
        print("Текущая скорость равна - ", self.__speed)
    
    def reverse(self):
        if self.__speed == 0:
            self.__speed = -5
            print("Текущая скорость равна - ", self.__speed)
        else: 
            self.__speed = -self.__speed
            print("Текущая скорость равна - ", self.__speed)
x1 = Car("Citroen","C5","2007")

while 1 == 1:
    print(f"""{x1.print_public_info()}1
    Выберите действие для вашей машины:
    1)Увеличить скорость
    2)Уменьшить скорость
    3)Остановить машину
    4)Показать текущую скорость
    5)Совершить разворот
    "q" - выйти из программы
    """)
    x1_1 = input()
    if x1_1 == "1":
        x1.speed_increase()
    if x1_1 == "2":
        x1.reduce_the_speed()
    if x1_1 == "3":
        x1.stop_car()
    if x1_1 == "4":
        x1.print_speed()
    if x1_1 == "5":
        x1.reverse()    
    if x1_1 == "q":
        break