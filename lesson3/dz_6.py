def int_func(word: str):
    """"Возвращение введеного слова с большой первой буквой"""
    first_letter = word[:1]
    big_first_leter = first_letter.upper()
    tail = word[1:]
    return big_first_leter + tail


def int_func2(line: str):
    """"Возвращение введеной строки слов с первыми большими буквами"""
    result = []
    words = line.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


row = input("Введите строку для преобразования:\n")
print(f"{int_func2(row)}")
