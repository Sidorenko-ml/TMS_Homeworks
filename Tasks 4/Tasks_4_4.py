# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1

Sp = [2,2,4,6,4,2,3,43,3,1,3513,1]
# Sp2 = []
# for el in Sp:
#     Sp2.append(el)
# if Sp2[0] == Sp[0]:
#     Sp2.append(Sp2[0])
#     Sp2.remove(Sp2[0])

# print(Sp2)

#Через функцию
def NewSp(list):
    Spisok = list.copy()
    Spisok.append(Spisok[0])
    Spisok.remove(Spisok[0])
    return Spisok

print(NewSp(Sp))

Sp2 = [2,4,5,12,52,13,4,5,2,15,6,7,444,231,4]
Sp2_1 = NewSp(Sp2)
print(Sp2_1)
print(NewSp(Sp2_1))