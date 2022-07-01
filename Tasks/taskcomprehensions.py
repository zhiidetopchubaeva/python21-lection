# task 1
list_= [item for item in range(1, 101)]
print(list_)
 
# task 2
list_ = [i for i in range(1, 50, 2)]
print(list_)

# task 3
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [num for num in list_ if num % 2 == 0 and num > 0]
print(int_list)

# task 4
list_ = [num ** 2 for num in range(1, 26)]
print(list_)

# task 5
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = [int(num) for num in str_list]
print(int_list)

# task 6
list_ = [num ** 2 if num % 2 == 0 else num for num in range(1,11)]
print(list_)

# task 7
list_ = [True if num % 2 == 0 else False for num in range(1,11)]
print(list_)

# task 8
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list = ['shorter' if len(i) <=4 else 'longer' for i in list_name]
print(new_list)

# task 9
dict_ = {num : num ** 2 for num in range(1, 11)}
print(dict_)

# task 10
n = int(input())
dict_={key: key ** 2 for key in range(1, 501) if key % n == 0}
print(dict_)

# task 11
a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {key: list(range(1, value + 1)) for key, value in a.items()}
print(dict_)

# task 12
dict_ = {'first': 1, 'second': 2, 'third': 3} 
a = {key: str(val).replace(f'{val}', 'even') if val % 2 == 0 else str(val).replace(f'{val}', 'odd') for key, val in dict_.items()}
print(a)

# task 13
string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
new_string = string_.split()
list_ = [num for num in new_string if num.isdigit()]
print(list_)

# task 14
dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
         'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
         'Nik': {'history': 84, 'math': 85, 'literature': 87}
         }

list1 = []
for k in dict_.keys():
    list1.append(k)

list2 = []
for k, v in dict_.items():
    for inner_k in v.keys():
        if inner_k == max(v, key = v.get):
            list2.append(inner_k)  
new_dict = {list1[index]: list2[index] for index in range(len(list1))}
print(new_dict)

# task 15

my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

list1 = []
for k, v in my_dict.items():
    list1.append(k)

list2 = []
for k, v in my_dict.items():
    for inner_k, inner_v in v.items():
        list2.append(inner_v)

dict_ = {list1[index]: list2[index] for index in range(len(list1))}
# dict_ = dict(zip(list1, list2))

print(dict_)

# task 16
list_ = [num / 2 for num in range(0, 11) if num % 2 == 0]
print(list_)

# task 17
dict_ = {1:'a', 2:'bro', 3:'re'}
res = {key:len(val) **3 if key % 2!=0 else len(val) for key,val in dict_.items()}
print(res)

# task 18 
set1 = {n1 for n1 in range(10)}
set2 = {n2 for n2 in range(8, 18)}

full_set = set1.union(set2)
length = len(list(full_set))

if length < 20:
    raznica = 20 - length
    print(f'В этом сете было {raznica} повторения, его длина составляет {length}')
else:
    print('Ваш объединенный сет полностью уникальный!')






