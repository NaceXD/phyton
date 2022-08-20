from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {float(self.param) / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):

    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * float(self.param) + 0.3 :.2f} ткани'


class Total:
    def __init__(self, s, h):
        self.s = s
        self.h = h

    @property
    def total(self):
        return f'Сумма затраченной ткани равна: {(float(self.s) / 6.5 + 0.5) + (2 * float(self.h) + 0.3) :.2f}'


size = input('Введите размер пальто: ')
height = input('Введиет рост костюма: ')

coat = Coat(size)
print(coat.consumption)

costume = Costume(height)
print(costume.consumption)

t = Total(size, height)
print(t.total)
