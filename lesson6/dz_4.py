class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} повернула на {direction}'

    def show_speed(self):
        return f'\nВаша скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name} '


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name}'


class PoliceCar(Car):
    pass


town = TownCar(input('Введите марку автомабиля: '), int(input('Введите скорость: ')), input('Введите цвет: '), False)
print('1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar(input('Введите марку автомабиля: '), int(input('Введите скорость: ')), input('Введите цвет: '), False)
print('2:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

work = WorkCar(input('Введите марку автомабиля: '), int(input('Введите скорость: ')), input('Введите цвет: '), False)
print('3:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

police = PoliceCar(input('Введите марку автомабиля: '), int(input('Введите скорость: ')), input('Введите цвет: '), True)
print('4:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())
