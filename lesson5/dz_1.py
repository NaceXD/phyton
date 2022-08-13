messages = list()

while True:
    message = input("Введите строку: ")
    if not message:
        break
    messages.append(message + "\n")
with open("text.txt", 'w', encoding='Utf-8') as my_txt:
    my_txt.writelines(messages)

with open('text.txt', 'r', encoding='Utf-8') as my_t:
    result = my_t.read()
    print(result)
