#3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). 
# Чтобы получить список ключей - использовать метод .keys()

Dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

def KeyLen(d1):
    d2=d1.copy() #надо копировать один объект (словарь) в другой, т.к. если присвоить через =, то при измененении первого будет меняться и второй
    for k1 in d1.keys():
        k2=k1+str(len(k1))
        d2[k2]=d1[k1]
        print(d2[k2])
        del d2[k1]
    return (d2)

print(KeyLen(Dict1))