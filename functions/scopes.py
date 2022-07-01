"===================Области видимости и пространства имен=============================="
locals() # - показыват все локальные переменные (возвращает словарь со всеми локальными переменными)
globals() # - показывает все глобальные переменные (возвращает словарь со всеми глобальными переменными)

# LEGB - local, enclosed, global, build-in

"Build-in" # - встроенное пространство имен( все встроенные переменные(input, print, sum, max. min, len, abs, int, str, dict ...))

"Global"  # - глобальное пространство имен( все переменные внутри файла, которыые создали мы)
# чтобы узнать что находится в глобальном пространстве, можно использовать функцию globals

"Local" # - какое-то закрытое пространство

"Enclosed" # - пространство, находящееся между двумя пространствами


def func(a, b):
    # локальное пространство
    a = 5
    print(a)
    print(locals())
func(5,2)


# print(a)  не может влиять на внутреннее пространство
# если вызвать в локальном глобальную выйдет результат, но если вызвать в гобальном локальную то не выйдет


# Компиляция – это сборка программы, включающая: трансляцию всех модулей программы, написанных на языке программирования высокого уровня, в эквивалентные программные модули на низкоуровневом языке, близком к машинному коду, или на машинном языке и сборку исполняемой программы.
# интерпретация - Когда вы пишете программу на языке Python, интерпретатор читает вашу программу и выполняет содержащиеся в ней инструкции. В действительности, интерпретатор - это слой программной логики между вашим программным кодом и аппаратурой вашего компьютера
# shell - это инструмент командной строки, который запускает интерпретатор python. Можно тестировать простые программы и также писать какие-то короткие программы. Однако для того, чтобы написать более сложную программу python нужен редактор. 


a = 10
d = 7

def func(b, c):
    # локальное пространство
    a = 5
    print(locals())
    # {'b': 5, 'c': 2, 'a': 5}
# func(5,2)

def func():
    # enclosed пространство
    a = "func"
    def inner_func():
        # local пространство
        a = "inner_func"
        print(locals()) # {'a': 'inner_func'}
    inner_func()
    print(locals()) # {'a': 'func', 'inner_func': <function func.<locals>.inner_func at 0x7fa171fa8d30>}

# func()

эртай = 'алиби'

def func():
    nastya = 'python21'
    print(эртай) # алиби

# func()
# print(nastya)   - NameError: name 'nastya' is not defined


count = 0

def add():
    print(count)
    count += 1 # UnboundLocalError: local variable 'count' referenced before assignment

def add():
    global count # доступ на изменение глобальной переменной count
    count += 1
    print(count)

add()
add()
add()
print(count)
# 1 2 3 3


a = 'global'

def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) # local
    
    print(a) # enclosed
    inner_func()

print(a) # global
outer_func()

# global enclosed local

a = 'global'
def outer_func():
    a = 'enclosed'
    print(a)

    def inner_func():
        a = 'local'
        print(a) # local
    
    inner_func()

outer_func()
print(a) # global
# enclosed local globals


def count(i):
    counter = 0
    
    def add():
        nonlocal counter # доступ на чтение и изменение локальной переменной counter 
        print(counter)
        counter += 1
    
    for _ in range(i):
        add()

count(10)
# 0 1 2 3 4 5 6 7 8 9

def func():
    a = '1'
    def inner_func():
        def inner2_func():
            nonlocal a # доступ на чтение и изменение локальной переменной a
            a = 2
        inner2_func()
    inner_func()
    print(a)
func() # 2