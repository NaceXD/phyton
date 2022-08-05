import copy


def get_person(name, last_name, year_of_birth, city, email, phone):
    """"Описывает Данные Пользователя"""
    print(f'Имя: {name}, Фамилия: {last_name}, Год рождения: {year_of_birth},'
          f'Город проживания: {city}, Email: {email}, Телефон: {phone}')


get_person(
    name=input("Введите Ваше Имя: "),
    last_name=input("Введите Вашу Фамилию: "),
    year_of_birth=int(input("Введите Ваш год рождение: ")),
    city=input("Введите Ваш город: "),
    email=input("Введите Ваш email: "),
    phone=int(input("Введите ваш номер: "))
)


def get_perosn2(**info):
    """"Описывает Данные Пользователя"""
    copy.copy(info)
    for k, v in info.items():
        return print("{}is {}".format(k, v))


get_person(
    name=input("Введите Ваше Имя: "),
    last_name=input("Введите Вашу Фамилию: "),
    year_of_birth=int(input("Введите Ваш год рождение: ")),
    city=input("Введите Ваш город: "),
    email=input("Введите Ваш email: "),
    phone=int(input("Введите ваш номер: "))
)
