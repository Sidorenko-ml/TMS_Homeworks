# 1.	Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, 
# если n — четное (n > 0 — параметр целого типа. 
# С помощью этой функции найти двойные факториалы пяти данных целых чисел [01-11.2-Proc35] 
from functools import reduce

def fact2(n):
    if n < 1:
        print("Было введено не натуральное число!")
    else:
        Spis = [i for i in range(1,n+1)]
        Chet = [i for i in Spis if i%2 == 0]
        Nechet = [i for i in Spis if i%2 != 0]
        if n % 2 == 0:
            res = reduce(lambda a, b : a * b, Chet)
        else:
            res = reduce(lambda a, b : a * b, Nechet)
    print(f"Двойной факториал числа {n} равен - ",res)
    return res
fact2(14)