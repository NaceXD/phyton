with open("dz6.txt", 'r', encoding='utf-8') as read_file:
    stats = {}
    read_lines = read_file.readlines()
    for line in read_lines:
        if len(line):
            subject = line.split()
            hours_sum = 0
            for hours in subject[1:]:
                if len(hours) > 1:
                    hours_sum += int(hours.split('(')[0])
            stats[subject[0]] = hours_sum
    print(f"Общее количество занятий по предметам:\n{stats}")
