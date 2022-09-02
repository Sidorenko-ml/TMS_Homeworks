from func import *

def ui_func():
    while 1 == 1:
        try:
            ch1 = float(input("Введите первый аргумент - "))
            ch2 = float(input("Введите второй аргумент - "))
        except Exception:
            print("Введены не числа")
        else:
            ch3 = input('Введите тип операции:\n1) +\n2) -\n3) *\n4) / \n')
            Func = Calc(ch1,ch2)
            if ch3 == '1':
                print(Func.summ())
            if ch3 == '2':
                print(Func.sub())
            if ch3 == '3':
                print(Func.mul())
            if ch3 == '4':
                print(Func.div())
            end = input("Продолжить? y/n \n")
            if end == 'y':
                continue
            if end == 'n':
                break