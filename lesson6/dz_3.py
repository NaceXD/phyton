class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=None):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


st = Position(input('Введите Имя: '), input('Введите Фамилию: '), input('Введите должность: '),
              input('Введите оклад: '), input('Введите премию: '))
print(st.get_full_name(), st.get_total_income())
