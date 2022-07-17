# Создать матрицу случайных чисел и сохранить ее в json файл. После прочесть ее, обнулить все четные элементы
# и сохранить в другой файл
from random import randint
import json

n = 3
Matrica = [[randint(1,40) for j in range(n)] for i in range(n)]

with open(r'C:\Users\sidor\TMS\Tasks 10\my_first_json.json','w') as file:
    json.dump(Matrica,file)

with open(r'C:\Users\sidor\TMS\Tasks 10\my_first_json.json','r') as file2, open(r'C:\Users\sidor\TMS\Tasks 10\my_json2.txt','w') as file3:
    data = json.loads(file2.read())
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] % 2 == 0:
                data[i][j] = 0
    file3.writelines(str(data))   #при записи данных в файл обязательно должен быть формат str