# numpy one D array syntax for linspace
# syntax : numpy.linespace( start, stop, num=50, endpoint=True, retstep=Flase, dtype=None, axis=0)

from numpy import *

#stu_rol = linespace(1, 200, num=50, endpoint=True)
#stu_rol = linspace(1,8)
# stu_rol = linspace(1,8,num=5)
stu_rol = linspace(1, 8, 5, endpoint=False)
a= len(stu_rol)

for nu in stu_rol:
    print(nu)

print('\n' "For loop with ranges")
for i in range(a):
    print(stu_rol[i])
    i+=1

print('\n' " While Loop")
i=0
while (i < a):
    print('index' , i, '=' ,stu_rol[i])
    i+=1
