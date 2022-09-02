# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена. 
# Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.

class Book():
    def __init__(self, number_of_pages, years, author,price):
        self.is_valid_number_of_pages = self._is_valid_number_of_pages(number_of_pages)
        self.years = self._is_valid_years(years)
        self.author = self._is_valid_author(author)
        self.price = self._is_valid_price(price)
    
    def _is_valid_number_of_pages(self,number_of_pages):
        if number_of_pages == str:
            raise TypeError("Количество страниц должно быть числом, а не строкой")
        if number_of_pages == float:
            raise TypeError("Количество страниц должно быть целым числом")
        if number_of_pages < 0:
            raise ValueError("Число страниц не может быть меньше 0")
        if number_of_pages == float:
            raise TypeError("")
        return number_of_pages


    def _is_valid_years(self,years):
        if not 0 < years < 2023:
            raise ValueError("Не может быть выпущена в это время")
        if years == str:
            raise TypeError("Год выпуска должен быть числом")
        if years == float:
            raise TypeError("Год выпуска должен быть числом")
        return years

    def _is_valid_author(self,author):
        if author == int:
            raise TypeError("Неверный формат ввода автора")
        if author == float:
            raise TypeError("Неверный формат ввода автора")
        return author
    def _is_valid_price(self,price):
        if price == str:
            raise TypeError("Неверный формат ввода цены")
        if price < 0:
            ValueError("Цена не может быть меньше нуля")
        return price
ex1 = Book(100,2001,'Stan Lee', 100)

ex2 = Book(245,1919,'Lev Tosltoy', 25)