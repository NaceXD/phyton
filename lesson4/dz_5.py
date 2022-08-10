from functools import reduce

new_list = [el for el in range(100, 1000+1) if el % 2 == 0]
print('Список четных чисел от 100 до 1000: \n', new_list)


def my_func(el_p, el):
    """Умножение чисел"""
    return el_p * el


print('Произведение этих чисeл: \n', reduce(my_func, new_list))
