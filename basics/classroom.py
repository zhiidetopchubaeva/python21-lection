import random
name = input('Введите ваше имя: ')
popytka = 0
vybor = input(f'{name} не хотите ли поиграть в "Угадай число"? Напишите "да" или "нет": ')
random_number = random.randint(1, 10)
if vybor == 'да':
    print('Число загадано')
    guess = -1
    popytka += 1
    while guess != random_number:
        guess = int(input('Введите число: '))
        if guess == random_number:
            continue_ = input(f'Поздравляю {name}! Вы угадали загаданное число, с {popytka} попытки.Хотите поиграть ещё раз? Напишите "да" или "нет": ')
            if continue_ == 'да':
                continue
            elif continue_ == 'нет':
                break
        elif guess != random_number:
            continue
elif vybor == 'нет':
    print('Хорошо, прощаемся')
print('До свидания!')




"""
1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
"""
with open('numbers.txt', 'w') as file:
  for num in range(1, 21):
    file.write(str(num) + '\n')


with open('squares.txt', 'w') as file1:
  with open('numbers.txt') as file:
    data_ = file.read().split('\n')
    data_.pop()
    new_data = list(map(int, data_))
    for num in new_data:
      file1.write(str(num ** 2) + '\n')  
    
"""
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
with open('usernames.txt', 'w') as file:
  while True:
    username = input('Введите имя пользователя (или слово End для окончания): ')
    if username == 'End':
      break
    file.write(f'Имя пользователя: {username}, длина: {len(username)}\n')