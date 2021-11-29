# 1
a = ['hello', '5', 'John']
b = ['Element', 'start', 'finish']
a.insert(0,b[0])
a.insert(1,b[1])
a.insert(len(a),b[-1])
print(a)

# 2

d = ['x', 5, 'John', 'honey'] 
lenght = len(d) 
 
 
def dict_(lenght): 
    a = {} 
    for i in range(lenght): 
        a[d[i]] = i + 1 
    print(a) 
 
 
dict_(lenght) 

# 3

def new_list(a, b): 
    g = [] 
    f = [] 
    for i in a: 
        if i % 2 == 0: 
            g.append(i) 
    for j in b: 
        k = pow(j, 2) 
        f.append(k) 
    return f, g 
 
 
a1 = [1, 2, 3, 4, 5] 
b1 = [1, 2, 3, 4, 5] 
a, b = new_list(a1, b1) 
print(a)
print(b)