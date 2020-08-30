# numpy one D array syntax for zeros
# syntax : numpy.zeros( shape,dtype=float,order='C')

from numpy import *

# stu_rol= zeros(5)

stu_rol= zeros(5,dtype=int)

for i in stu_rol:
    print(i)

print('\n', " For loop with zeros")

j=0
nu =len(stu_rol)
for j in range(nu):
    print('index', j, '=', stu_rol[j])

print('\n', " While with zeros")
k=0
while k < nu:
    print('index', k, '=', stu_rol[k])
    k+=1
