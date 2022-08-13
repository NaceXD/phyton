import json

data = [{}, {}]
data[1]['average_profit'] = 0
with open('dz7.txt', 'r', encoding='utf-8') as file:
    file.readline()
    num = 0
    for line in file:
        print(line.split())
        num += 1
        name = line.split()[0]
        profit = float(line.split()[2]) - float(line.split()[3])
        data[0][name] = profit
        data[1]['average_profit'] += profit
    data[1]['average_profit'] /= profit
with open('dz7.json', 'w', encoding='utf-8') as j_file:
    json.dump(data, j_file)
