def s():
    try:
        with open('new_txt.txt', 'w', encoding='utf-8') as f_cont:
            enter = input('Введите цифры через пробел:')
            f_cont.writelines(enter)
            numb = enter.split()

            print('Сумма введеных чисел: ', sum(map(int, numb)))
    except IOError:
        return IOError
    except ValueError:
        return ValueError


s()
