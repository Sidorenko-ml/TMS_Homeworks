# 8) В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы. [02-7.2-HL08]

str = 'В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы'
strrev = " ".join(reversed(str))
print(strrev)

# Либо с помощью среза сразу перевернуть строку:
str2 = 'В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы'[::-1]
print(str2)