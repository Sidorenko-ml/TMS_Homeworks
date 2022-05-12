#1) Дан список целых чисел. 
#Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2
#Необходимо сделать двумя способами,через while и for

Spisok = [1,5,3,4,6,7,8,4,3,6,55,3,3]
Sp2 = []
for i in Spisok:
    Sp2.append(i*(-2))
print(Sp2)

NewSp = []
while len(NewSp) != len(Spisok):
    for item in Spisok:
        NewSp.append(item * (-2))
    break
print(NewSp)

print(Spisok[1])