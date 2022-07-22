my_list = (
    1, 2, 'Список', [1, 2], {'name': 'Alex', 'age': 22}, True, None, (13, 12, 26), set('1231231'), 2.4, complex(2, 4))
for i in range(len(my_list)):
    print(f'Переменная: {type(my_list[i])}')
