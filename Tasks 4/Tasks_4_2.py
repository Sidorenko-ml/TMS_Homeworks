#2) Дан список целых чисел. Подсчитать сколько четных чисел в списке

Sp = [1,3,4,5,6,3,2,215,6,74,3,143423,123,123,4,56,7,2,35,6,72,3,5,67,43,233,422]
Sp2 = []
Sp3 = []
for i in Sp:
    Sp2.append(i%2)
for item in Sp2:
    if item ==0:
        Sp3.append(i)
print('Количество четных чисел равно: ',len(Sp3))
print(Sp2)