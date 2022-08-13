with open('txt.txt', 'r+', encoding='utf-8') as file:
    my_list = list()
    for line in file.readlines():
        my_list.extend(line.split(' '))
print(my_list)

rus_lst = ["Один", "Два", "Три", "Четыре"]

j = 0
for i in range(0, len(my_list), 3):
    my_list[i] = rus_lst[j]
    j += 1

print(my_list)
with open('txt_rus.txt', 'w', encoding='utf-8') as out_f:
    out_f.writelines(my_list)
