from operator import index
from random import randint

from numpy import mat

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
print("Индекс колонки с максимальной суммой элементов - ", column.index(max(column)))
print("Индекс ряда с минимальной суммой элементов - ", sum_of_row.index(min(sum_of_row)))
print("Индекс колонки с минимальной суммой элементов - ", column.index(min(column)))
for item in Matrica:
    Matrica[0][1] = 0
    Matrica[0][2] = 0
    Matrica[1][2] = 0
print(Matrica)
for item in Matrica:
    Matrica[1][0] = 0
    Matrica[2][0] = 0
    Matrica[2][1] = 0
print(Matrica)

matrix_a = [[randint(1,100) for i in range(n)] for item in range(n)]
matrix_b = [[randint(1,65) for i in range(n)] for item in range(n)]
print(matrix_a)
print(matrix_b)

matrix_c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        matrix_c[i][j]=matrix_a[i][j]+matrix_b[i][j]
print("Матрица, полученная сложением созданых выше matrix_a и matrix_b: ",matrix_c)

matrix_d = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        matrix_d[i][j]=matrix_a[i][j]-matrix_b[i][j]
print("Матрица, полученная c помощью разницы созданых выше matrix_a и matrix_b: ",matrix_d)
