def my_func():
    """Выводит числа начиная с введеного заканчивает на 10"""
    num = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(num), 10):
        print(i)


my_func()


def my_func2():
    """"Выводит числа повтором из списка заканчивает на 10 повторении"""
    my_list = [1, 2, 15, 3, 20]
    from itertools import islice
    from itertools import cycle
    for el in islice(cycle(my_list), 10):
        print(el)


my_func2()
