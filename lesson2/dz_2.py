my_list = []
for i in range(int(input('Введите длину списка: '))):
    my_list.append(input('Введите значение: '))
print(my_list)
if my_list == 1:
    print(my_list)
else:
    x = 0
    for i in range(int(len(my_list) / 2)):
        my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]
        x += 2
print(my_list)
