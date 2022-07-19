"==============Инкапсуляция================"
# Инкапсуляция - принцип ООП
# 1. сокрытие данных (ограничение доступа к определенным методам и классам)
# 2. сбор всех необходимых для класса методов и аттрибутов в "капсулу" (класс)

"==================== Модификаторы доступа к аттрибутам ===================================="
# 1 public (публичный)
# 2 protected (защищенный)
# 3 private (приватный)

# class A:
#     attr = "публичный"
#     _attr2 = "защищенный"
#     __attr3 = "приватный"


# A.attr # публичный
# A._attr2 # защищенный
# A.__attr3 # AttributeError: type object 'A' has no attribute '__attr3'
# A._A__attr3 # приватный

"========================== getters/setters ================================="
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property # TypeError: 'int' object is not callable
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception("age can not be less than 0 or more than 120")


obj = Person("Zhiide", 28)
# print(obj.__age) # AttributeError: 'Person' object has no attribute '__age'
print(obj.age) # 28
obj.age = -5 # 
print(obj.age)

class A:
    __a = "kksjwssj"

    def get_a(sel):
        return self.__a

    def set_a(self):
        return