def my_sum(my_list):
    """"Преобразование в число с плавующей точкой"""
    items = 0
    for item in my_list:
        try:
            items += float(item)
        except ValueError:
            continue
    return items


def sum_string(s):
    """"Сумма строк"""
    s = s.replace('q', '')
    s = s.replace(',', '.')
    numbers = s.split(' ')
    return my_sum(numbers)


result = 0

while True:
    enter = input("Введите строку чисел через пробел. Для завершения введите символ 'q'\n")
    result += sum_string(enter)
    if result != 0:
        print(f"Сумма значений элементов {result}")
    if enter.count('q') > 0:
        break
