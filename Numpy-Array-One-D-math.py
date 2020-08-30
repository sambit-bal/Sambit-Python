from numpy import *

a = array([100,101,102,103,104,105])
a = a + 5
b = array([10,11,12,13,14,15])
b = b - 5

print(a)
print(b)

for i in a:
    print('index', '=',i)

print()
for j in b:
    print('index','=',j)

print()
d= a + b
print(d)