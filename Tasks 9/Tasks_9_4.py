# 4.	Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный. 
def flip(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper

@flip
def ReturnSnach(x,y):
    print(x,y)
