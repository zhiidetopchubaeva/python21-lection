# ЗАДАНИЕ 1

# ЗАДАНИЕ 2
a = {'a': 1, 'b': 2, 'c': 1}
print(a.pop('b'))

# ЗАДАНИЕ 3
a = {'a': 1, 'b': 2, 'c': 1}
b = {'f': 55}
a.update(b)
print(a)

# ЗАДАНИЕ 4
a = {'a': 1, 'b': 2, 'c': 1}
dict.clear(a) 
print(a)

# ЗАДАНИЕ 5
a = {'a': 1, 'b': 2, 'c': 1}
b = list(a.keys())
print(b)

# ЗАДАНИЕ 6
a = {'a': 1, 'b': 2, 'c': 1}
b = a.copy()
print(b)

# ЗАДАНИЕ 7
a = {'a': 1, 'b': 2, 'c': 1}
for b in a.keys():
    print(b)

# ЗАДАНИЕ 8
a = {'a': 1, 'b': 2, 'c': 1}
for b in a.values():
    print(b)
# ЗАДАНИЕ 9
a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = {}
for key in a:
    value = a[key]
    if value % 2 == 0:
        b[key] = 2
    else: 
        b[key] = value
print(b)

# ЗАДАНИЕ 10

# ЗАДАНИЕ 11 
a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key, val in a.items():
    new_val = val / 5
    a.update({key: new_val})

print(a)



