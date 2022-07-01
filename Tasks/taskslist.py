# ЗАДАНИЕ 1
name_of_friends = ['Mira', 'Dasha', 'Ais', 'Guka', 'Aika']
i = 0 
while i < len(name_of_friends): 
    print(name_of_friends[i]) 
    i += 1
# второй вариант
name_of_friends = ['Mira', 'Dasha', 'Ais', 'Guka', 'Aika']
for k in name_of_friends:
    print(k)
 
# ЗАДАНИЕ 2
labels = ['Honda', 'Suzuki', 'Yamaha', 'Kawasaki']
for k in labels:
    print(f'I like brand', k)

# ЗАДАНИЕ 3
name_of_list = ['Hellozhiide']
half_length = int((len(name_of_list[0])) / 2)
chast1 = name_of_list[0][:half_length]
chast2 = name_of_list[0][half_length:]
if int(len(name_of_list[0])) % 2 != 0:
    half_length = int(len(chast1)) + 1
new_chast1 = name_of_list[0][0:half_length]
new_chast2 = name_of_list[0][half_length:]
new_list = new_chast2 + new_chast1
print(list(new_list)) # ['h', 'i', 'i', 'd', 'e', 'H', 'e', 'l', 'l', 'o', 'z']

# ЗАДАНИЕ 4
list_ = ['Zhiide', 'Topchubaeva']
new_list = [list_[-1], list_[0]]
print(new_list)

# ЗАДАНИЕ 5
suitcase = []
suitcase.append('футболка') 
suitcase.append('шорты') 
suitcase.append('сланцы') 
suitcase.append('очки') 
suitcase.append('кепка') 
suitcase.pop(-1)
suitcase.insert(0, 'панама')
print(suitcase)

# ЗАДАНИЕ 6 
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = [numb for numb in nums if numb < 5]
print(res)

# ЗАДАНИЕ 7
numbers = input().split(',')
list_ = list(numbers)
tuple_ = tuple(numbers)
print(list_)
print(tuple_)

# ЗАДАНИЕ 8
list_ = [1, 2, 3, 4, 5]
list1 = str(list_[0]), str(list_[1]), str(list_[2]), str(list_[-2]), str(list_[-1])
new_list = list(list1)
print(new_list) # можно так тоже решить, или можно использовать for, while как ниже приведу

list_ = [1, 2, 3, 4, 5]
new_list = []
for x in list_:
    new_list.append(str(x))
print(new_list)

# ЗАДАНИЕ 9
list_ = [1, 2, 3, 4, 5]
new_list = []
for number in list_:
    if number % 2 == 0:
        new_list.append('четное')
    elif number % 2 != 0:
        new_list.append('нечетное')   
print(new_list)   

# ЗАДАНИЕ 10
list_ = list(range(20))
print(list_)
# или можно задать начало и конец, и шаг по которому надо двигаться
list_ = list(range(10, 50, 2))
print(list_)

# ЗАДАНИЕ 11
list_ = list(range(0,101,2))
for i in list_:
    print(i)

# ЗАДАНИЕ 12
list1 = [11, 23, 45, 7, 9] 
list2 = [21, 4, 16, 8, 10] 
list3 = list1 + list2 
new_list = sum(list3)
print(new_list)
 
# ЗАДАНИЕ 13
list_ = input().split(',')
list_.sort()
print(list_)

# ЗАДАНИЕ 14
list_ = [1, 1, 3]

if len(set(list_)) != len(list_):
    print('yes')
else:
    print('ERROR')

# ЗАДАНИЕ 15
list_ = []
for i in range(54, 9185):
    if i % 5 == 0:
        list_.append(i)
print(list_)




