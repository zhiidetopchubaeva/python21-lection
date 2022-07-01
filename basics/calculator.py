# #Калькулятор
# a = float(input('Введите первое число: ')) # может пользователь будет вводить не целые числа
# b = float(input('Введите второе число: '))
# c = input('Выберите операцию из следующих +-*/%**// : ')
# if c == "+" :
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "*":
#     print(a * b)
# elif c == "/":
#     print(a / b)
# elif c == "%":
#     print(a % b)
# elif c == "**":
#     print(a ** b)
# elif c == "//":
#     print(a // b)
# else:
#     print('Данной операции нет в системе')



#"Виселица"

import random
def vicelitsa():
    print('Привет! Добро пожаловать в игру Виселица')
    words_ = ['мандарин','яблоко', 'груша', 'виноград', 'апельсин', 'даманго']
    secret = random.choice(words_)
    guess = 'ауоиыэюяёе'
    popytka = 5

    while popytka > 0:
        missed = 0
        for bukva in secret:
            if bukva in guess:
                print(bukva, end= ' ')
            else:
                print('_', end= ' ')
                missed += 1
        if missed == 0:
            print('\nТы выиграл!')
            break

        guess1 = input('\nНазови букву: ')
        guess += guess1

        if guess1 not in secret:
            popytka -= 1
            print('\nНе угадал!')
            print('\nОсталось попыток: ',popytka)
            if popytka < 5: print('\n  | ')
            if popytka < 4: print('\n  O ')
            if popytka < 3: print('\n /|\ ')
            if popytka < 2: print('\n  | ')
            if popytka < 1: print('\n / \ ')
            if popytka == 0: print('\n\nЭто слово: ',secret)

otvet = 'да'
while otvet == 'да':
    vicelitsa()
    print('Хочешь сыграть снова? (да или нет)')
    otvet = input()



# attempts = 10
# word = input('Введите слово: ').strip(' ').lower()
# splitted_word = list(word)

# dogadka = ['_' for i in splitted_word]

# while True:
#     print(' '.join(dogadka))
#     print('Осталось попыток: ', attempts)
#     bukvy = input('Введите букву: ').strip(' ').lower()
#     if bukvy in splitted_word:
#         for i, x in enumerate(splitted_word):
#             if x == bukvy:
#                 dogadka[i] = bukvy
#         if '_' not in dogadka:
#             print('Вы выиграли!')
#             break
#     else:
#         attempts -= 1
   
#     if attempts == 0:
#         print('Вы проиграли! Загаданное слово: ', word, '- Вас повесили')
#         print()
#         break

# print(' '.join(dogadka))    