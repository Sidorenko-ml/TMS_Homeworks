# #Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.
# [03-15.16]

File1 = open(r'C:\Users\sidor\TMS\test.txt.txt', 'r', encoding='utf-8')

# firstline = next(File1).strip() - можно с помощью next(f).strip()
# firstline = File1.readline().strip() - можно с помощью простого readline со strip()

line1 = File1.readlines(1)
print(line1[0].replace('\n',''))

line5 = File1.readlines(5)
print(line5[0].replace('\n',''))

line1to5 = File1.readlines()[:5]
for i in line1to5:
    print(i.replace('\n',''))

line1to2 = File1.readlines()[0:2]
for i in line1to2:
    print(i.replace('\n',''))

All = File1.read()
print(All)

File1.close()