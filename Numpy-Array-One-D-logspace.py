# numpy one D array syntax for logspace
# syntax : numpy.logspace( start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)

from numpy import *

# stu_rol=logspace(1,5)
# stu_rol=logspace(1,5,5,base=10.0)
stu_rol= logspace(1, 3, 5)
n = len(stu_rol)

for nu in stu_rol:
    print(nu)

print('\n', " For loop with range")
for i in range(n):
    print(stu_rol[i])
    i+=1

print('\n', "While loop with logspace")
i=0
while i<n:
    print('index',i, '=',stu_rol[i])
    i+=1
