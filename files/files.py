"============Работа с файлами====================="
# open - функция, которая позволяет открыть файл
"==============Режимы========================"
# r - read только для чтения
# w - write только для записи (сначала все из файла удаляется,а потом записывается)
# a - append дозапись(все новое добавляется в конец)
# x - создает файл, если он уже существует - ошибка
# rb - чтение в бинарном виде
# wb - запись в бинарном виде
# ab - дозапись в бинарном виде

# open("test.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
"когда мы не указываем режим - по умолчанию чтение"

# open("test.txt", "w") - создает пустой файл
"когда мы открываем файл в режиме w - он создает пустой файл и потом "

# open("test.txt", "a")
"когда файла нет - он создает его"

# file = open("test.txt", "w")
# res = file.read()
# print(res)
# io.UnsupportedOperation: not readable 
# метод read нельзя использовать при режиме записи и дозаписи

"=============== READ ======================"
# file = open("test.txt", "r") # открываем файл в режиме чтения
# res = file.read() # считывает весь файл и возвращает строку
# print(res)
# Hello world
# Makers Bootcamp
# line1
# line2
# line3

# file = open("test.txt")
# res = file.read()
# print(file.read(5)) # пустая строка, потому что каретка находится в самом конце файла
# file.seek(0) # каретка переходит в индекс 0(в начало файла)
# print(file.read(5)) # "hello" считал 5 символов
# print(file.read(5)) # " worl" считал следующие символы, тк мы уже находились на 5м символе
# print(file.tell()) # 10  показывает текущее положение каретки
# res = file.readlines()
# print(res) # ['d\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
# file.seek(0)
# print(file.readlines()) # ['Hello world\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
# file.seek(0)
# print(file.readlines(35)) # ['Hello world\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n']  он читает то количество которую мы задали, и возвращает только эти символы
# # print(file.tell())
# file.close()


"=============== WRITE ======================="
# file = open("test.txt", "w")
# file.write("Hello world\n") # в файл записали строку hello world
# file.write("Makers Bootcamp\n") # после этого продолжает писать строку Makers Bootcamp

# file.writelines(["line1\n", "line2\n", "line3\n"]) # writelines принимает список со строками и дозаписывает их в файл
# file.close() # обязательно закрываем файл



"================ WITH ======================="
# with - конструкция, которая в начале конструкции вызывает метод __enter__, а в конце вызывает __exit__

# class Test:
#     def __enter__(self):
#         print("Начало работы")
#         return self

#     def __exit__(self, *args, **kwargs):
#         print("Конец работы")

#     def hello(self):
#         print("Hello world")

# with Test() as test:
#     test.hello()
# Начало работы
# Hello world
# Конец работы


# file1 = open("test.txt", "w")
# file1.write("hello")
# file2 = open("test.txt", "w")
# file2.write("world")
# file1.write("hbfjfhf")
# # worldhbfjfhf

# file1 = open("test.txt", "w")
# file1.write("hello")
# file1.close() # закрыли файл1
# file2 = open("test.txt", "w")
# file2.write("world")
# # file1.write("hbfjfhf")
# # ValueError: I/O operation on closed file, т.к. мы закрыли файл1
# file2.close()

# file = open("test.txt", "w")
# file.write("Hello world\nMakers\nBootcamp")
# file.seek(0)
# file.write("New lines")
# # New linesld
# # Makers
# # Bootcamp

# file = open("test.txt", "w+")
# file.write("Hello world\nMakers\nBootcamp")
# file.seek(0)
# res = file.read()
# file.seek(0)
# file.write("New lines")
# file.write(res)
# # New linesHello world
# # Makers
# # Bootcamp
# file.close()
# print(file.closed) # True


with open("test.txt") as file:
    print(file.read()) 
    print(file.closed) # False
print(file.closed)     # True
# New linesHello world
# Makers
# Bootcamp
