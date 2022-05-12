#2) Дано число. Найти сумму и произведение его цифр.

def SumAndProiz():
    Ch = int(input("Введите любое число - "))
    Ch2 = list(str(Ch))
    sum = 0
    proiz = 1
    if len(Ch2) == 1:
        proiz = 0
    for i in Ch2:
        sum += int(i)
        proiz *= int(i)
    print(f'Сумма цифр в числе равна = {sum}')
    print(f'Произведение цифр в числе равно = {proiz}')
SumAndProiz()
