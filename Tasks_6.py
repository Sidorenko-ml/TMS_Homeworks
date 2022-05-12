import enum
from operator import index
from random import randint
from xmlrpc.client import Marshaller
n = 3
print("Дана матрица случайных чисел:")
Matrica = [[randint(1,40) for i in range(n)] for item in range(n)]
print(Matrica)
MaxElem = []
for item in Matrica:
    for i in item:
        MaxElem.append(i)
print("Максимальный элемент матрицы - ",max(MaxElem))
print("Минимальный элемент матрицы - ",min(MaxElem))
Sum_of_elements = sum(MaxElem)
print('Сумма всех элементов - ',Sum_of_elements)
sum_of_row = []
for item in Matrica:
    sum_of_row.append(sum(item))
print(sum_of_row)
print("Индекс ряда с максимальной суммой элементов - ", sum_of_row.index(max(sum_of_row)))