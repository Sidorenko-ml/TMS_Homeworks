#5.	Создать строку равную всем элементам введенной строки с четными индексами. 
# (считая, что индексация начинается с 0, поэтому символы выводятся 
# начиная с первого, индексы 0,2,4,6….).

strk = str(input('Введите строку с любыми значениями: '))
new_str = strk[0::2]
print(new_str)