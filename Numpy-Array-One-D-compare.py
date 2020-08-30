from numpy import *

a = array([100,101,102,103,104,105])
b = array([10,11,102,13,1004,15])

result = a == b
result_1 = a < b

for i in result:
    print('value', '=', i)

print()

for j in result_1:
    print('value', '=', j)