# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
# [03-15.29]

with open(r'C:\Users\sidor\TMS\Tasks 10\Novosti.txt', 'r',encoding='utf-8') as file:
    file1 = [i.replace('\n','') for i in file.readlines()]
    file2 = []
    file3 = []
    for num, i in enumerate(file1,1):
        if num % 2 == 0:
            file2.append(i)
        else:
            file3.append(i)
    