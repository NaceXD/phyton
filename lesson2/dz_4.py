text = input('Введите ваш текст через пробел: ')
word = text.split()
for x, y in enumerate(word, start=1):
    if len(y) > 11:
        y = y[:10]
        print(x, y)
    else:
        print(x, y)
