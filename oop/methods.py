


class A:
    def  instance_method(self):
        print("Метод объекта")

obj_a = A()
obj_a.instance_method() # вызываем у объекта, и он автоматически попадает как аргумент в метод
# Метод объекта
A.instance_method(obj_a) # вызываем у класса, нужно передать объект
# Метод объекта

# class methods (методы класса) - метод, который принимает первым аргументом cls (класс). Чтобы создать метод класса, нужно метод задекорировать @classmethod

class A:
    @classmethod
    def class_method(cls):
        print(cls) # <class '__main__.A'>
        print("Метод класса") # Метод класса

A.class_method() # <class '__main__.A'>
A().class_method() # Метод класса

class Pizza:

    def __init__(self, radius, *ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def cook(self):
        print(f"Пицца размером {self.radius} см\nИнгредиенты:\n{self.ingredients}")

    @classmethod
    def pepperoni(cls, radius):
        return cls(radius, "Пепперони", "помидоры")

    @classmethod
    def four_cheeze(cls, radius):
        cls(radius, "Моцарелла", "Дор блю", "Еще сыр", "И Еще сыр")

pizza1 = Pizza(30, "Сыр", "помидоры", "грибы")
pizza2 = Pizza.pepperoni(30)
pizza3 = Pizza.pepperoni(35)
pizza4 = Pizza.four_cheeze(25)
pizza5 = Pizza.four_cheeze(40)


pizzas = [pizza1, pizza2, pizza3]
for pizza in pizzas:
    pizza.cook()


# Static методы - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом

class Square:
    def __init__(self, a):
        self.a = a 
        self.s = self.get_s(a)

    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s) # 16

