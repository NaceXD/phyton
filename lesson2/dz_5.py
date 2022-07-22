given_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите количество новых чисел: '))
if new_el > 0:
    for i in range(1, new_el + 1):
        new_numb = int(input('Введите новое число:'))
        if new_numb > 0:
            given_list.append(new_numb)
            given_list.sort(reverse=True)
            print(given_list)
        else:
            print('Ошибка!!!Введите натуральное число: ')
else:
    print('Ошибка!!!!Введите натуральное число')
