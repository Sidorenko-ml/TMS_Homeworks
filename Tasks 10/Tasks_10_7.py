# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот

with open(r'C:\Users\sidor\TMS\test.txt.txt','r', encoding='utf-8') as file1, open(r'C:\Users\sidor\TMS\Tasks 10\Tasks10_7.txt','w') as files2:
    file1 = file1.readlines()
    file2 = [i.replace('0','1') for i in file1]
    files2.writelines(file2)