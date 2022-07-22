month = int(input('Введите число месяца: '))
seasons_list = ('Зима', 'Весна', 'Лето', 'Осень')
while True:
    if month > 12 or month <= 0:
        print('Введённое вами число не коректно.Пожалуста введите месяц от 1 до 12: ')
        month = int(input('Введите число месяца: '))
        continue
    elif month == 12 or 1 <= month < 3:
        print(f"Введеный вами месяц '{month}' относится к '{seasons_list[0]}'")
        break
    elif 3 <= month < 6:
        print(f"Введеный вами месяц '{month}' относится к '{seasons_list[1]}'")
        break
    elif 6 <= month < 9:
        print(f"Введеный вами месяц '{month}' относится к '{seasons_list[2]}'")
        break
    else:
        print(f"Введеный вами месяц '{month}' относится к '{seasons_list[3]}'")
        break
