# Создать пять классов описывающие реальные объекты. Каждый класс должен содержать минимум три приватных атрибута, конструктор,
# геттеры и сеттеры для каждого атрибута, два метода

from io import BufferedRandom
from operator import ge


class Phone:
    def __init__(self, brand, model, color, IMEI1 = None):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__IMEI1 = IMEI1    
    
    def phone_on(self):
        print("Телефон включен")

    def open_settings(self):
        print("Открыты настройки")

    def set_brand(self,brand):
        self.__brand = brand
    
    def set_model(self,model):
        self.__model = model
    
    def set_color(self,color):
        self.__color = color
    
    def set_IMEI(self,IMEI1):
        self.__IMEI1 = IMEI1

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    
    def get_IMEI(self):
        return self.__IMEI1


class Laptop:
    def __init__(self, brand, model, serial_number = None):
        self.__brand = brand
        self.__model = model
        self.__serial_number = serial_number
    
    def laptop_on(self):
        print("Ноутбук включен")

    def auto_off(self, time_in_hours, time_in_min):
        print(f"Ноутбук автоматически будет выключен в {time_in_hours}:{time_in_min}")

    def set_brand(self,brand):
        self.__brand = brand
    
    def set_model(self,model):
        self.__model = model
        
    def set_IMEI(self,serial_number):
        self.__serial_number = serial_number

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_serial_number(self):
        return self.__serial_number

class Bycicle:
    def __init__(self,brand, type, wheels, number_of_speeds):
        self.brand = brand
        self.__type = type
        self.__wheels = wheels
        self.__number_of_speeds = number_of_speeds

    def ride(self):
        print("Велосипед едет")

    def change_speeds(self):
        print("Переключена скорость")

    def set_brand(self,type):
        self.__type = type
    
    def set_model(self,wheels):
        self.__wheels = wheels
        
    def set_IMEI(self,number_of_speeds):
        self.__number_of_speeds = number_of_speeds

    def get_type(self):
        return self.__type
    
    def get_wheels(self):
        return self.__wheels
    
    def get_number_of_speeds(self):
        return self.__number_of_speeds

class Book:
    def __init__(self, author, year_of_writing, genre, number_of_pages):
        self.__author = author
        self.__year_of_writing = year_of_writing
        self.__genre = genre
        self.__number_of_pages = number_of_pages

    def read(self, page):
        print("Книга открыта на странице - ", page)

    def close(self, str):
        print(f"Оставить закладку на {str} стр.")

    def set_author(self, author):
        self.__author = author
    def set_years(self, year_of_writing):
        self.__year_of_writing = year_of_writing
    def set_genre(self, genre):
        self.__genre = genre
    def set_number_of_pages(self, number_of_pages):
        self.__number_of_pages = number_of_pages
    
    def get_author(self):
        return self.__author
    def get_years(self):
        return self.__year_of_writing
    def get_genre(self):
        return self.__genre
    def get_number_of_pages(self):
        return self.__number_of_pages

class VacuumCleaner:
    def __init__(self, brand, model, type):
        self.__brand = brand
        self.__model = model
        self.__type = type
    
    def start_clean(self):
        print("Начинается уборка!")
    
    def stop_clean(self):
        print("Уборка завершена")
    
    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model
    def set_type(self,type):
        self.__type = type
    
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_type(self):
        return self.__type
    
