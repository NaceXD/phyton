def my_func(x, y):
    """"Возведение числа х в степень у через **"""
    return x ** abs(y)


print(my_func(int(input("Введите число х: ")), int(input("Введите отрицательное число y: "))))


def my_func2(x, y):
    """"Возведение числа х в степень у через цикл"""
    i = 1
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    print(result)


my_func2(int(input("Введите число х: ")), int(input("Введите отрицательное число y: ")))
