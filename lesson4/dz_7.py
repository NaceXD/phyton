from math import factorial


def fact(n):
    """Программа вычисления факториала числа"""
    for i in range(1, n+1):
        print(i, end='! = ')
        yield factorial(i)


for el in fact(4):
    print(el)
