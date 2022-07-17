#3.	Дан файл, содержащий различные даты. Каждая дата - это число, месяц и год. Найти самую раннюю дату. [02-8.1-ML-29

from datetime import datetime

file = open(r'C:\Users\sidor\TMS\Tasks 10\years.txt.txt', 'r')
dates = file.readlines()
file.close()

dates2 = [i.replace('\n','') for i in dates]
dates2.sort(key = lambda date: datetime.strptime(date, '%d.%m.%Y'))
print('Самая ранняя дата -',dates2[0])