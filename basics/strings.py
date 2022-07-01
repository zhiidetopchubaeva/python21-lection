"строки" 
# строки - неизменяемый тип данных, который предназнаен для хранения текста(последовательности символов), заключенного в одинарные или двойные кавычки
# синтаксис: 
string1 = "строка с одинарными кавычками"
string2 = "строка с двойными кавычками"
# error = 'неправильная строка"
string3 = "Dont't " # внутри двойных кавычек все одинарные- просто символы
string4 = 'Maker"s bootcamp' # внутри одинарных кавычек все двойные- просто символы
# print(string1, string2, string3, string4)
string5 = '''
многострочный текст в одинарных(двойных) кавычках. Тут можно ставить "любые" 'кавычки'  """"""" но не тройные, т.к. будет искать тройную для закрытия
'''
string7 = 'hello' + ' ' + 'world' # 'hello world'
string8 = 'A' 
"Экранизация строк"
# экранизация спец-символов
'\n' # перенос на новую строку
'\t' # табуляция 
'\\' # отображение \ (потому что он является инструкцией, которая влияет на наш код), чтобы вывести двойные надо будет четыре раза набрать '\\\\'
'\''  # отображение '(кавычки)
'\r' # возвращает каретку  print('первое слово привет\rвторое цветочек')  получилось слово "второe цветочекивет"
'\v' #  перенос на новую строку сосмещением вправо на длину предыдущей строки
# например  
'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\nworld'
# hello 
# world

'hello\tworld'
# hello      world
 
'чтобы экранировать нужен символ \\'
 # чтобы экранировать нужен символ \

'hello\vworld'
# hello
#       world

"форматирование строк"
title = 'Плов'
price = 1500
# f'Название: Плов, Цена: 1500' - надо обозначать переменные, и взять их в фигурные скобки
f'Название: {title}, Цена: {price}'

format1 = f'Название: {title}, Цена: {price}'
format2 = 'Название: %s, Цена: %s'
# %s пока не знаем 
print(format2 % ("Гуляш", "250"))
print(format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250' 
# Название: Самсы, Цена: 70' 


format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35' 

"методы строк"
# методы типов данных - функции, к которым мы обращаемся через точку
dir(str) # позволяет посмотреть все методы класса(типов данных)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'hello'.title() # 'Hello'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'
'hello'.center(11) # '    hello    '
'hello'.center(11, '-') # '---hello---'
'hello'.count('l') # 2
'hello'.count('ll') #  1
'hello hello'.count('hello') # 2
'hello'.count('w') # 0

'hello world'.startswith('hello') # true
'hello world'.startswith('H') # False
'hello world'.endswith('ld') # true

'hello world'.find(' ') # 5
'hello world'.find('o') # 4
'hello world'.find('wo') # 6
'hello world'.find(' hello') # 0

'hello world'.split() # ['hello', 'world']
'hello world'.split(o) # ['hell', ' w', 'rdld']
'$'.join(['hello', 'world']) # 'hello$world'
''.join(['hello', 'world']) # 'helloworld'
' '.join('hello world'.split()) # 'hello world'


"конкетинация"
# это склеивание строк
'hello' + 'world' # 'helloworld'
'hello' + '' + 'world' # 'hello world'

 

"Индексы"
# индексы - порядковый номер символа в строке
'h e l l o   w o r l d '
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # ' '

#срез - подстрока строки
string[0:5] # 'hello'
string[0:6] # 'hello '
string[2:4] # 'll'
string[0:5] [2:4]# 'll' выполнит 1 команду + в ней вторую команду

string[:5] # 'hello'
string[6:] # 'world'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd'
string[::3] # 'hlwl'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh'




"доп инфа"
a = 5
b = 5
print(id(a))
print(id(b))
print(hash(a))
print(hash(a))
id(a) ==id()








