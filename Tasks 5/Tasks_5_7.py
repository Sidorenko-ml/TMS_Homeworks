# 7) Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]

from random import randint
n = 3
Matr = [[randint(1,25) for j in range(n)] for i in range(n)]
print("Дана целочисленная квадратная матрица: ", Matr)
for i in Matr:
    Matr[0][0] = max(Matr[0])
    Matr[1][1] = max(Matr[1])
    Matr[2][2] = max(Matr[2])
print(Matr)