# 1.	Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст. Создать отчетный файл
#  с информацией по количеству людей входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+. 

import csv

with open( 'Tasks10_1.csv' , mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ";")
    writer.writerow(['Имя','Фамилия','Возраст'])
    writer.writerow(['Олег','Сидоренко','24'])
    writer.writerow(['Ольга','Сидоренко','30'])
    writer.writerow(['Владимир','Федотов','49'])
    writer.writerow(['Леонид','Слуцкий','50'])

A_1_12 = []
A_13_18 = []
A_19_25 = []
A_26_40 = []
A_40b = []

with open('Tasks10_1.csv' , 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if 1 <= int(row['Возраст']) <= 12:
            A_1_12.append('1')
        if 13 <= int(row['Возраст']) <= 18:
            A_13_18.append('1')
        if 19 <= int(row['Возраст']) <= 25:
            A_19_25.append('1')
        if 26 <= int(row['Возраст']) <= 40:
            A_26_40.append('1')
        if int(row['Возраст']) > 40:
            A_40b.append('1')    

print('В возрастную группу в возрасте от 1 до 12 входит ' + str(len(A_1_12)) + ' чел')
print('В возрастную группу в возрасте от 13 до 18 входит ' + str(len(A_13_18)) + ' чел')
print('В возрастную группу в возрасте от 19 до 25 входит ' + str(len(A_19_25)) + ' чел')
print('В возрастную группу в возрасте от 26 до 40 входит ' + str(len(A_26_40)) + ' чел')
print('В возрастную группу в возрасте более 40 лет входит ' + str(len(A_40b)) + ' чел')

