from random import randint
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