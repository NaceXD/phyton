def division(num_1, num_2):
    """Деление двух чилел"""
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return 'Ошибка деление на 0'


print(division(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
