# Задание 6
# Создать три целых числа x, y, z.
# Выведите значение наименьшего из них.
# К примеру, если в переменных у нас числа: 102, 36, 90, вывод в терминал будет 36

# x = 3
# y = 5
# z = 9
# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else: 
#     print(z)

# Задание 7

# Создать три целых числа в переменных x, y, z. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 - если все числа совпадают,
# 2 - если два числа совпадают
# 0 - если все три числа разные.

# Например, если в переменных у нас числа - 32, 32 и 100, вывод будет:2 

# x = 34
# y = 56
# z = 44
# if x == y == z:
#     print(3)
# if x == y or y == z or x == z:
#     print(2)
# else:
#     print(0)

# Задание 8

# В переменные x, y попадают числа вводимые пользователем. Проверить делится ли первое число на второе без остатка.
# Программа должна вывести на экран следующую информацию:
# частное - выводить в любом случае
# если число делится с остатком, вывести остаток от деления
# Например, если во вкладке INPUT ввести числа 675 и 23, вывод должен быть:
# x не делится на y
# Частное: 29
# Остаток: 11
# если в переменные получили числа 10 и 2, вывод должен быть
# x делится на y
# Частное: 5


# x = int(input())
# y = int(input())
# if x % y == 0:
#     print("%d делится на %d" % (x,y))
#     print("Частное: %d" % (x//y))
# else:
#     print("%d не делится на %d" % (x,y))
#     print("Остаток: %d" % (x%y))
#     print("Частное: %d" % (x//y))

# mistakes here  

# Задание 9
# В переменную year попадает число-год от пользователя.
# Определите, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Note: в соответствии с григорианским календарем, год является високосным в двух случаях: 1) если число года делится без остатка на 4 и НЕ делится на 100, 2) либо число года делится без остатка на 400.
# Например, если в INPUT введен год 1996, вывод должен быть:
# YES 
# т.к число 1996 делится без остатка на 4, но не делится на 100

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# Задание 10
# Создайте список чисел nums и число target.
# С помощью условных операторов выведите, есть ли число в этом списке, если есть выведите в консоль Да, если нет выведите Нет.
# Например, если дан список [1, 15, 36, 88], а в переменной target хранится число 15, вывод будет:
# Да 

# nums = [4, 3, 6, 8, 9, 7]
# target = 9
# if target in nums:
#     print('Да')
# else:
#     print('Нет')

# Задание 11

# В переменную num из вкладки INPUT попадает число, которое обозначает код символа по таблице ASCII(https://ru.wikipedia.org/wiki/ASCII)
# Определить, является ли введенное число кодом английской буквы.
# Если число является кодом буквы, вывести сообщение:
# Это буква "буква" 
# в ином случае, вывести сообщение:
# Это не буква, а символ "символ" 
# Например, если число num равно 43:
# Это не буква, а символ "+"
# Для числа 65:
# Это буква "А"
# найдите и используйте специальную функцию Python, возвращающую числовое значение Unicode элемента

# num = int(input())
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# if a<=num<=z or A<=num<=Z:
#     print('Это буква', chr(num))
# else:
#     print('Это не буква, а символ', chr(num))  
# mistake with ""

# ЗАДАНИЕ 12

# В переменную greeting попадает строка из поля во вкладке INPUT
# Если пользователь вводит Hi, то программа должна ответить Привет!.
# Во всех других случаях вывести строку NO.
# Пример, если в поле ввели Hi:
# "Привет!"
# если ввели что-то другое, например "Hello":
# "NO"

# greeting = input()
# if greeting == 'Hi':
#     print('Привет!')
# else:
#     print('NO')

# Задание 13
# Объявите переменную count, значение которой равно 0
# Из вкладки INPUT в переменную number попадает строка состоящая из числа.
# Проверьте строку в переменной number. Если строка number состоит из числа, то преобразуйте данную строку в числовой тип данных и запишите результат в count.
# Распечатайте значение count.
# Например, если ввели "0", то count перезапишется на 0:
# 0 
# если ввели строку "5", то count будет равен:
# 5
# если же, в INPUT ввели "10", распечатав count получим:
# 10

count == 0
number = int(input())
if number.isdigit():
    print()





