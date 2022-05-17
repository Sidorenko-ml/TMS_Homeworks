# 1.	Написать 12 функций по переводу:
# 1.	Дюймы в сантиметры
# 2.	Сантиметры в дюймы
# 3.	Мили в километры
# 4.	Километры в мили
# 5.	Фунты в килограммы
# 6.	Килограммы в фунты
# 7.	Унции в граммы
# 8.	Граммы в унции
# 9.	Галлон в литры
# 10.	Литры в галлоны
# 11.	Пинты в литры
# 12.	Литры в пинты

from operator import lt


def dm_sm(x):
    Ch = x * 2.54
    if (x%10) == 1:    
        print(f'{x} дюйм = {Ch} см')
    if 1 < (x%10) <= 4:    
        print(f'{x} дюйма = {Ch} см')
    if (x%10) >= 5:    
        print(f'{x} дюймов = {Ch} см')
    return Ch

def sm_dm(x):
    Ch = x * 0.393701
    if (Ch % 10) == 1:    
        print(f'{x} см = {Ch} дюйм')
    if 1 < (Ch % 10) <= 4:    
        print(f'{x} см = {Ch} дюйма')
    if (Ch % 10) >= 5:    
        print(f'{x} см = {Ch} дюймов')
    return Ch

def mile_km(x):
    Ch = x * 1.60934
    if (x % 10) == 1:    
        print(f'{x} миля = {Ch} км')
    if 1 < (x % 10) <= 4:    
        print(f'{x} мили = {Ch} км')
    if (x % 10) >= 5:    
        print(f'{x} миль = {Ch} км')
    return Ch

def km_mile(x):
    Ch = x * 0.6214
    if (Ch % 10) == 1:    
        print(f'{x} км = {Ch} миля')
    if 1 < (Ch % 10) <= 4:    
        print(f'{x} км = {Ch} мили')
    if (Ch % 10) >= 5:    
        print(f'{x} км = {Ch} миль')
    return Ch

def ft_kg(x):
    Ch = x * 0.4536
    if (x % 10) == 1:    
        print(f'{x} фунт = {Ch} кг')
    if 1 < (x % 10) <= 4:    
        print(f'{x} фунта = {Ch} кг')
    if (x % 10) >= 5:    
        print(f'{x} фунтов = {Ch} кг')
    return Ch

def kg_ft(x):
    Ch = x * 2.2046
    if (Ch % 10) == 1:    
        print(f'{x} кг = {Ch} фунт')
    if 2 <= (Ch % 10) <= 4:    
        print(f'{x} кг = {Ch} фунта')
    if (Ch % 10) >= 5:    
        print(f'{x} кг = {Ch} фунтов')
    return Ch

def un_gr(x):
    Ch = x * 28.349523125
    if (x % 10) == 1:    
        print(f'{x} унция = {Ch} гр')
    if 2 <= (x % 10) <= 4:    
        print(f'{x} унции = {Ch} гр')
    if (x % 10) >= 5:    
        print(f'{x} унций = {Ch} гр')
    return Ch

def gr_un(x):
    Ch = x * 0.03527396195
    if (Ch % 10) == 1:    
        print(f'{x} гр = {Ch} унция')
    if 2 <= (Ch % 10) <= 4:    
        print(f'{x} гр = {Ch} унции')
    if (Ch % 10) >= 5:    
        print(f'{x} гр = {Ch} унций')
    else:
        print(Ch,"oz")
    return Ch

def gal_ltr(x):
    Ch = x * 4.5461
    print(f'{x} гал = {Ch} л')
    return Ch

def ltr_gal(x):
    Ch = x * 0.22
    print(f'{x} л = {Ch} гал')
    return Ch

def pnt_ltr(x):
    Ch = x * 0.5683
    if (x % 10) == 1:    
        print(f'{x} пинта = {Ch} л')
    if 2 <= (x % 10) <= 4:    
        print(f'{x} пинты = {Ch} л')
    if (x % 10) >= 5:    
        print(f'{x} пинт = {Ch} л')
    return Ch

def ltr_pnt(x):
    Ch = x * 1.7598
    if (Ch % 10) == 1:    
        print(f'{x} л = {Ch} пинта')
    if 1 < (Ch % 10) <= 4:    
        print(f'{x} л = {Ch} пинты')
    if (Ch % 10) >= 5:    
        print(f'{x} л = {Ch} пинт')
    return Ch

while 1 == 1:
    print('Здравствуйте, какую конвертацию вы хотите выполнить?\n1.	Дюймы в сантиметры\n2.	Сантиметры в дюймы\n3.	Мили в километры\n4.	Километры в мили\n5.	Фунты в килограммы\n6.	Килограммы в фунты\n7.	Унции в граммы\n8.	Граммы в унции\n9.	Галлон в литры\n10.	Литры в галлоны\n11.	Пинты в литры\n12.	Литры в пинты')
    a1 = int(input("Введите номер операции, либо нажмите 0 для выхода - "))
    if (a1 == 0):
        break
    if (a1<1) or (a1>12):
        print('Такой операции не существует!')
        a3 = str(input("Желаете продолжить? y/n "))
        if a3 == 'y':
            continue
        if a3 == "n":
            break
    x1 = int(input("Введите число - "))
    if a1 == 1:
        dm_sm(x1)
    if a1 == 2:
        sm_dm(x1)
    if a1 == 3:
        mile_km(x1)
    if a1 == 4:
        km_mile(x1)
    if a1 == 5:
        ft_kg(x1)
    if a1 == 6:
        kg_ft(x1)
    if a1 == 7:
        un_gr(x1)
    if a1 == 8:
        gr_un(x1)
    if a1 == 9:
        gal_ltr(x1)
    if a1 == 10:
        ltr_gal(x1)
    if a1 == 11:
        pnt_ltr(x1)
    if a1 == 12:
        ltr_pnt(x1)
    a2 = str(input("Желаете продолжить? y/n "))
    if a2 == 'y':
        continue
    if a2 == "n":
        break