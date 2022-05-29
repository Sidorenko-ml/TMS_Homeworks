# 3.	Создать декоратор для функции, которая принимает список чисел.
#  Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.

def DelChet(func):
        def  Delete(args):
            newsp = [i for i in args if i % 2 == 0]
            return func(newsp)
        return Delete

@DelChet
def PrinSpis(x):
    print(x)

Spis = [2,412413,32423,123,432,5436346,123123,4234324,123,323241424,12323,43,23231,3234,2]

PrinSpis(Spis)