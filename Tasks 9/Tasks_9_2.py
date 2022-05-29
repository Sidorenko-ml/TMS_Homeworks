# 2.	Создать lambda функцию, которая принимает на вход
# неопределенное количество именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

slov = lambda **kvargs: {key*2:value for key,value in kvargs.items()}
print(slov(abc=5, odindvatri=123))
