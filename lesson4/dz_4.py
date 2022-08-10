new_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
r_list = [el for el in new_list if new_list.count(el) == 1]
print('Исходный список: ', new_list)
print('Результат', r_list)
