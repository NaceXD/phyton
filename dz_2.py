sec_time = int(input('Введите количество секунд: '))
hours = sec_time // 3600
if hours < 10:
    r_hours = '0' + str(hours)
else:
    r_hours = hours
minutes = (sec_time % 3600) // 60
if minutes < 10:
    r_minutes = '0' + str(minutes)
else:
    r_minutes = minutes
seconds = (sec_time % 3600) % 60
if seconds < 10:
    r_seconds = '0' + str(seconds)
else:
    r_seconds = seconds
    # print(f'Время по МСК: {r_hours}:{r_minutes}:{r_seconds}')
if r_hours > 24:
    print('Введите коректное время')
else:
    print(f'Время по МСК: {r_hours}:{r_minutes}:{r_seconds}')