# 4) Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. 
from functools import reduce

try:
    N = int(input("Введите любое натуральное число - "))
    if N < 1:
        print("Не натуральное число")
    else:
        list1 = [i for i in range(2,N+1)]
        S = reduce(lambda a,x: a + 1/x, list1, 1)
        print(S)
except(Exception):
    print("Вы ввели неверное значение!!!")