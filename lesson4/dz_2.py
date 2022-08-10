import random

result_list = []
new_list = [int(i) for i in input('Введите список чисел: ').split()]
for i in range(0, len(new_list)):
    if new_list[i] > new_list[i - 1]:
        (result_list.append(new_list[i]))

"""new_list = [int(i) for i in input('Введите список чисел: ').split()]
for i in range(1, len(new_list)):
    if new_list[i] > new_list[i - 1]:
        (result_list.append(new_list[i]))"""
print('Исходный список: ', new_list)
print('Список, элементы которого больше предыдущего: \n', result_list)

result_list2 = []
random_list = random.sample(range(1, 9999), 20)
for i in range(0, len(random_list)):
    if random_list[i] > random_list[i - 1]:
        (result_list2.append(random_list[i]))
"""result_list2 = []
random_list = random.sample(range(1, 9999),20)
for i in range(1, len(random_list)):
    if random_list[i] > random_list[i - 1]:
        (result_list2.append(random_list[i]))"""
print('Исходный список: ', random_list)
print('Список, элементы которого больше предыдущего: \n', result_list2)
