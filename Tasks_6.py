import enum
from operator import index
from random import randint
from xml.dom.expatbuilder import theDOMImplementation
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
print("Индекс ряда с максимальной суммой элементов - ", sum_of_row.index(max(sum_of_row)))
one_col = [Matrica[0][0],Matrica[1][0],Matrica[2][0]]
second_col = [Matrica[0][1],Matrica[1][1],Matrica[2][1]]
three_col = [Matrica[0][2],Matrica[1][2],Matrica[2][2]]
column = [sum(one_col),sum(second_col),sum(three_col)]
print("Индекс колонок с максимальной суммой элементов - ", column.index(max(column)))
print("Индекс ряда с минимальной суммой элементов - ", sum_of_row.index(min(sum_of_row)))
print("Индекс колонок с минимальной суммой элементов - ", column.index(min(column)))