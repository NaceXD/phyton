import re

stats = {}

with open('dz6.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        row_items = row.split(': ')
        hours = re.findall(r"\d+", row_items[1])
        stats.update({row_items[0]: sum([int(i) for i in hours])})


print(f"Общее количество занятий по предметам:\n{stats}")
