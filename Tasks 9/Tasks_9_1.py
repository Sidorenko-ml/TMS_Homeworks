# 1.	Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, 
# где i это порядковый номер строки в списке. Использовать генератор списков.

Spis = ["Первая строка","second string",'Google Chrome',"Belhard Academy","Teach me Skills","Visavis","BEL SMART ORANGE","Xioami"]
Sp = [f'{index} - {i}' for index, i in enumerate(Spis)]
print(Sp)