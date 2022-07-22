products = []
product_names = []
product_prices = []
product_counts = []
product_units = []
enter = None
while enter != 'q':
    print('Добро пожаловать!')
    print('Добавить новый товар: +')
    print('Посмотреть аналитику товаров: a')
    print('Выход: q')
    enter = input('В какой раздел хотите перейти: ')
    if enter == 'a':
        analytics = {
            'Наименование товара': list(set(product_names)),
            'Цена товара': list(set(product_prices)),
            'Количество товара': list(set(product_counts)),
            'eд': list(set(product_units))
        }
        print(f"Отчет по списку товаров: \n{analytics}")
    elif enter == '+':
        new_add = int(input('Введите количество новых товаров: '))
        for i in range(new_add):
            print(f"Заполняем информацию по {i + 1}-му товару")
            name = input('Наименование товара: ')
            price = int(input('Цена товара: '))
            count = int(input('Количество товара: '))
            unit = input('Единица измерения: ')
            products.append(
                (i + 1, {'Наименование товара': name, 'Цена товара': price, 'Количество товара': count, 'eд': unit}))
        print(f"Исходный список товаров: \n{products}")
        for i in products:
            product_names.append(i[1].get('Наименование товара'))
            product_prices.append(i[1].get('Цена товара'))
            product_counts.append(i[1].get('Количество товара'))
            product_units.append(i[1].get('eд'))
