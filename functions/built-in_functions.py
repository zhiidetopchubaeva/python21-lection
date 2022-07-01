"=============Built-in functions========================="

"lambda" # анонимная функция  
#lambda параметры: что функция возвращает

add = lambda a, b: a + b
print(add) # <function <lambda> at 0x7f6c65ad3dc0>  неправильно 
print(add(5,4)) # 9

"map" # функция, которая принимает первым аргуменом функцию, а вторым итерируемый объект. map возвращает генератор, в котором все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности

map_gen = map(int, ['1', '2', '3', '4'])
print(map_gen)  # <function <lambda> at 0x7f6c65ad3dc0>
print(list(map_gen)) # [1, 2, 3, 4]


res = list(map(lambda a: a + 1, [1,2,3,4,5]))
print(res) # [2, 3, 4, 5, 6]

"=================map на цикле for====================="
func = lambda a: a + 1
res = []

for e in [1, 2, 3, 4, 5]:
    res.append(func(e))
print(res) #  [2, 3, 4, 5, 6]

"filter" # функция, которая возвращает генератор, принимает функцию и итерируемый объект. Результатом будет последовательность из элементов итерируемого объекта, которые прошли фильтр(проверку)

list_ = [' "Ertai', 'Oomat', 'Argen', 'Manas', 'Bekzat', 'Daniel', 'Erkaiym']

def startswith_vowels(name):
    vowels= 'AEOIUYАЕЁИУЭЮЯЫ'
    if name[0].upper() in vowels:
        return True
    return False
res = list(filter(startswith_vowels, list_))
print(res) # ['Oomat', 'Argen', 'Erkaiym']

def startswith_vowels(name):
    vowels= 'AEOIUYАЕЁИУЭЮЯЫ'
    return name.upper().startswith(tuple(vowels)) 
     
res = list(filter(startswith_vowels, list_))
print(res) # ['Oomat', 'Argen', 'Erkaiym']

"================filter на цикле for ======================="
def startswith_vowels(name):
    vowels = 'УЕЁЫАОЭЯИЮEYUOAI'
    return name.upper().startswith(tuple(vowels))

list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниэль", "Эркайым"]

res = []
for name in list_:
    if startswith_vowels(name):
        res.append(name)
print(res) # ["Эртай", "Оомат", "Арген", "Эркайым"]

"reduce" # нужно импортировать из библиотеки functools 
# эта функция принимает функцию и итерируемый объект и возвращает 1 результат

from functools import reduce 
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mul(a, b):
    return a * b
res = reduce(mul, list_)
print(res) # 362880


"=====================Reduce на цикле for ================================"

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mul(a, b):
    return a * b

res = list_[0]

for b in list_[1:]:
    res = mul(res, b)

print(res) # 362880


"enumerate" # функция, которая принимает последовательность. Она возвращает генератор, в которой каждый элемент - tuple состоящий из числа и элемента из последовательности
# enumerate нумерует элементы начиная с нуля
list_ = ['a', 'b', 'c', 'd']

for i in enumerate(list_):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index, elem in enumerate(list_):
    print('index -', index, ' : ', 'elem -', elem)
# index - 0  :  elem - a
# index - 1  :  elem - b
#  # index - 2  :  elem - c
# index - 3  :  elem - d

list_ = ['a', 'b', 'c', 'd']
for i in enumerate(list_[1:]):
    print(i)
# (0, 'b')
# (1, 'c')
# (2, 'd')

list_ = ['a', 'b', 'c', 'd']
for i in enumerate(list_[1:], 10):
    print(i)
# (10, 'b')
# (11, 'c')
# (12, 'd')

"zip" # соединяет последовательности

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(list1, list2))) 
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
print(dict(zip(list1, list2))) 
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}


list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c"]
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
print(list(zip(list1, list2, list3)))
# [(1, 'a', 1.9), (2, 'b', 2.7), (3, 'c', 3.0), (4, 'd', 4.5)]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
list4 = [(1,2), (3,4)]
print(list(zip(list1, list2, list3, list4)))
# [(1, 'a', 1.9, (1, 2)), (2, 'b', 2.7, (3, 4))]

