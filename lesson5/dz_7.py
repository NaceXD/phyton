import json

stat = [{}, {}]
stat[1]['average_profit'] = 0
with open('dz7.txt', 'r', encoding='utf-8') as file:
    file.readline()
    numb = 0
    for line in file:
        print(line.split())
        numb += 1
        name = line.split()[0]
        profit = float(line.split()[2]) - float(line.split()[3])
        stat[0][name] = profit
        stat[1]['average_profit'] += profit
    stat[1]['average_profit'] /= profit
with open('dz7.json', 'w', encoding='utf-8') as j_file:
    json.dump(stat, j_file)
