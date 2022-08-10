from sys import argv

wages, output_in_hours, rate_per_hour, prize = argv

print('\n<< Программа рассчета заработной платы сотрудника >>')
print('Количество часов: ', output_in_hours)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', prize)
print('Зарплата сотрудника состовляет: ', (float(output_in_hours) * float(rate_per_hour)) + float(prize))
