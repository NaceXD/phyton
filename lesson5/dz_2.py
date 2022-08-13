def my_f():
    try:
        with open('n_text.txt', 'r', encoding='utf-8') as m_file:
            m_list = m_file.readlines()
            for i in range(len(m_list)):
                n_list = m_list[i].split()
                print(f'Количество строк в файле: {len(m_list)}. В {i + 1}-ой строке - {len(n_list)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


def my_func():
    try:
        with open('n_text.txt', 'r', encoding='utf-8') as my_txt:
            content = my_txt.read()
            content = content.split()
            print(f'Общее количество слов в файле - {len(content)}')
    except FileNotFoundError:
        return 'Файл не найден.'


my_f()
my_func()
