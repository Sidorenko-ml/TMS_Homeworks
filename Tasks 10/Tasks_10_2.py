# 2.	Создать csv файл с данными о ежедневной погоде.
#  Структура:  Дата, Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.
from base64 import decode
import csv

with open('Tasks10_2.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Дата','Место','Градусы, С','Скорость ветра, м/с'])
    writer.writerow(['05.06.2022','Минск','20','4.3'])
    writer.writerow(['06.06.2022','Минск','20','5.1'])
    writer.writerow(['07.06.2022','Минск','20','4.6'])
    writer.writerow(['08.06.2022','Минск','21','4.4'])
    writer.writerow(['09.06.2022','Минск','22','5.3'])
    writer.writerow(['10.06.2022','Минск','21','4.1'])
    writer.writerow(['11.06.2022','Минск','21','5.8'])

temp = []
Speed = []

with open('Tasks10_2.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        temp.append(int(row['Градусы, С']))
        Speed.append(float(row['Скорость ветра, м/с']))

print(temp)

def SumSr7days(x):
    sum = 0
    for i in x:
        sum+=int(i)
    return(sum/7)

def SumSr7daysFloat(x):
    sum = 0
    for i in x:
        sum+=float(i)
    return(sum/7)

print("Средняя температура в Минске за последние 7 дней -",SumSr7days(temp))
print("Средняя скорость ветра в Минске за последние 7 дней -",SumSr7daysFloat(Speed))