class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


def st():
    while True:
        enter = input('Введите название канцелярия: ')
        if enter == 'Pen' or enter == 'Ручка':
            pen = Pen('ручкой')
            print(pen.draw())
            break
        elif enter == 'Pencil' or enter == 'Карандаш':
            pencil = Pencil('карандашем')
            print(pencil.draw())
        elif enter == 'Handle' or enter == 'Маркер':
            handle = Handle('маркером')
            print(handle.draw())
        else:
            print('Ошибка!!!\nВведите из следующих значений:'
                  '(Pen,Pencil,Handle или Ручка,Карандаш,Маркер)')


st()
