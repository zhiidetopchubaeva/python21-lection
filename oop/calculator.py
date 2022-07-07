class Calc:
    def __init__(self, color):
        self.color = color

    def add(self, a, b):
        "Функция сложения"
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def true_div(self, a, b):
        "Функция целочисленного деления"
        return a // b

    def mod(self, a, b):
        "функция нахождения остатка от деления"
        return a % b
    
    def divmod(self, a, b):
        "Функция возвращает целое число и остаток  от деления"
        return self.true_div(a, b), self.mod(a, b)

    
    def pow(self, a, b):
        "Функция возведения числа в степень"

    def sqrt(self, a, ndigits=2):
        "Функция нахождения квадратного корня числа"
        # return a ** 0.5
        import math
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, ndigits)

    def percent(self, total, _percent):

        return (total * _percent) / 100

    def __str__(self):
        return f"{self.color} калькулятор"

    def super_func(self, string):
        "Выполнит все,что угодно"
        return eval(string)

obj1 = Calc("Синий")
obj2 = Calc("Фиолетовый")
obj1.add(4, 5) # 9
obj2.add(4, 5) # 9

print(eval(input()))

