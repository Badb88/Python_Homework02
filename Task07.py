# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Факториал 5! = 120

print()
def Factorial(b):
    res = 1
    for i in range(1, b):
        res *= b
        b -= 1
    return res

a = int(input('Введите число: '))
res = Factorial(a)
print(f'{a}! = {res}')