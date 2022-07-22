month = int(input('Введите число месяца: '))
seasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
monts_dict = {1: seasons.get(1), 2: seasons.get(1), 12: seasons.get(1),
              3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
              6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3),
              9: seasons.get(4), 10: seasons.get(4), 11: seasons.get(4)}
if month in monts_dict:
    value = monts_dict[month]
    print(f"Введеный вами месяц '{month}' относится к '{value}'")
else:
    print('Введённое вами число не коректно.Пожалуста введите месяц от 1 до 12')
