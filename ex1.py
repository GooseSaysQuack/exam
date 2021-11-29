# 1 str
x = str(int(float(5)))

# 2 str
x = 'aa' == 'AA'

# 3 dict
x = {i: i**2 for i in range(5)}

# 4 set
x = set(list((5, 6, 7)))

# 5 NoneType
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)
print(type(x))

# 6 list
x = [].append('j')

# 7 если < 5 тип str, в ином случае int
for i in range(10):
    if i < 5: x = 'hello'
    else: x = 5 

# 8 str
x = input('Enter and integer: ')

# 9 list
a = 5 
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b

# 10 str
def func(x, y=5): return x + y
x = func('Jaguar ', 'hunter')