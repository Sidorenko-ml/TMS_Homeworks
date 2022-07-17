# Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки. Если нет, то получить номер первой строки, 
# в которой эти файлы отличаются друг от друга.

with open(r'C:\Users\sidor\TMS\Tasks 10\file1_for_Tasks10_9.txt','r', encoding='utf-8') as file1, open(r'C:\Users\sidor\TMS\Tasks 10\file2_for_Tasks10_9.txt', 'r',encoding='utf-8') as file2:
    fileN1 = file1.readlines()
    fileN2 = file2.readlines()
    count = 0
    eq = True
    for a1,a2 in zip(fileN1,fileN2):
        count += 1
        if a1 != a2:
            eq = False
            print(f'Номер строки, которая не совпадает - {count}')
            break

