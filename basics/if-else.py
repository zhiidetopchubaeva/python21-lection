"=============Логические операторы==============="
# логические операторы - выражения, которые возвращают True, если правда, False - если ложь

5 == 5 # True
4 == 5 # False

5 != 5 # False не равно
5 != 2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

'5' = 5 # False  тк первое строка, второе число


"Bool type"
# булевый тип данных - имеет 2 значения True, False
bool(1) # True
bool(0) # False только 0 будет давать False
bool(-277) # True

bool('hello') # True
bool('') # False
bool(' ') # True тк здесь есть пробел

bool(True) # True
bool(False) # False


"None Type"
# None - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствия значения
bool(None) # False
bool('None') # True тк внутри строка, 

a = None
print(bool(a)) # False тк a = None
print(a is None) # True тк is это проверка на полное соответствие
# is проверяет ячейки памяти


"Условные операторы"
# условные операторы нужны для того, чтобы приразных входных данных од работал по разному

if условие1:
    тело1
    # будет работать только если условие1 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
else:
    тело2
    # будет работать если условие1 не верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать если условие1 не верно и условие2 верно
else:
    тело3
    # будет работать если условие1 не верно и условие2 не верно

# в одной конструкции мы можем использовать неограниченное кол-во elif 
# в одной конструкции мы можем использовать только 1 if
# else мы можем использовать только 1 раз или не использовать вообще

a = int(input('Введите число: '))

if a > 0:
    print(f'Число {a} - положительное')
elif a < 0:
    print(f'Число {a} - отрицатеьное')
else a = 0:
    print(f'Число {a} - это 0')

"FizzBuzz"
# выведите числа от 1 до 100
# если число кратно 3 - вывести Fizz
# если чимло кратно 5 - вывести Buzz
# если число кратно и 5 и 3- вывести FizzBuzz
# если число не кратно и 5 и 3- вывести  число


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'вывести FizzBuzz')
    elif i % 3 == 0:
        print(f'вывести Fizz')
    elif i % 5 == 0:
        print(f'вывести Buzz')
    else:
        print(i)

#второй способ решения задачи
for i in range(1, 101):
    if i % 3 == 0:
            if i % 5 == 0:
                print('вывести FizzBuzz')
            else: print('Fizz')    
    elif i % 5 == 0:
        print('вывести Buzz')
    else:
        print(i)



"Тернарные операторы"
# условие в олну строку
тело1 if условие else тело2

res = 'Hello' if a == 5 else 'Bye'
print(res)
# Hello если a = 5
# Bye если a !=5

