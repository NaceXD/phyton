class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Некоректный год'
            else:
                return f'Некоректный месяц'
        else:
            return f'Некоректный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('24-08-2022')
print(today)
print(Data.valid(11, 12, -10000))
print(today.valid(11, 13, 2013))
print(Data.extract('11-11-2011'))
print(today.extract('11-11-2020'))
print(Data.valid(1, 11, 2000))
