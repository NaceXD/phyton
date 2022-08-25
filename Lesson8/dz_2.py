class MyException(Exception):
    @classmethod
    def my_func(cls, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


primer = MyException()

primer.my_func(1, 2)
primer.my_func(1, 0)
primer.my_func(-1, 3)
primer.my_func(0, 4)
