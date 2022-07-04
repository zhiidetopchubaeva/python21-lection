"================= OOP =============================="
# OOP - object-oriented programming(объектно-ориентированное программирование - парадигма)

class Person:
    name = "Zhiide"
    age = 28
    arms = 2
    legs = 2

    def __init__(self, name, age):
        """
        функция, которая вызывается когда мы создаем объект от класса
        self - ссылка на созданный объект
        """
        self.name = name # Мы создаем в объект  self новый аттрибут name
        self.age = age # новый аттрибут age


    def walk(arg):
        print("Я иду")

    
    def add_age(obj):
        obj.age += 1

    def __str__(self):
        """
        функция, которая вызывается, когда мы оборачиваем объект в класс str или когда принтуем объект
        функция __str__ ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return f"{self.name} - {self.age} y.o."
# person1 = Person()
# print(person1.age) # 28
# print(person1.arms) # 2
# person1.walk() # Я иду 
# person1.add_age()
# # Person.add_age(person1) # Старый вариант предыдущей строки
# print(person1.age) # 29

# person2 = Person()
# print(person2.age) # 28 т.к. они не меняют класс, а просто копируют. т.е  person1 скопировал класс Person(),а не изменил его вид

# Person.age = 18
# print(Person.age) # 18

# person2 = Person()
# print(person2.age) # 18

person1 = Person("Nastya", 50)
print(person1.age) # 50

person2 = Person("Zharkynai",23)
print(person2.age) # 23



