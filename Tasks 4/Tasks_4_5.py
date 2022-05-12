#5) Составить список чисел Фибоначчи содержащий 15 элементов.

# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

def Fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return Fibonacci(i-2) + Fibonacci(i-1)

for x in range(15):
    print(Fibonacci(x))    
