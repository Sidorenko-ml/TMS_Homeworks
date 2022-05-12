#Задача: создать функцию, которая суммирует все получаемые на вход позиционные аргументы

from re import I
from turtle import st


def SummArgs(*args:int):
    s = list(args)
    Summa = 0
    for item in s:
        Summa += item
    return Summa

sum = SummArgs(2,3,4,5,6)
print(sum)
# Для решения этой задачи мне пришлось из кортежа сделать список. Только после этого проводить какие-либо операции, т.к. кортеж
# хранит в себе неизменяемые данные. *args - изначально кортеж

#Но можно было сделать проще :(
def NSumm(*args):
    summ = 0
    for i in args:
        summ = summ + i
    return summ

Pr = NSumm(2,4,5,6,10)
print(Pr)
#Проще говоря, можно суммировать данные в кортеже таким образом.


#Задача удалить повторяющиеся дважды и более объекты.
spis1 = [2,4,5,4,2,3,4,3,1,6]

def Fupo(lst):
    NewSp = []
    for item in lst:
        if lst.count(item)<2:
            NewSp.append(item)
    return NewSp
        
Proba = Fupo(spis1)
print(Proba)

#Нужно просуммировать все цифры в числе а
a = 3456
b = list(str(a))
result = 0
for i in b:
    result += int(i)
print(result)
