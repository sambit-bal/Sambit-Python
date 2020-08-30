# numpy one D array syntax for ones()
# syntax : numpy.ones( shape,dtype=float,order='C')

from numpy import *

stu_rol = ones(5,dtype=int)

for i in stu_rol:
    print(i)

print('\n', "For with range")

nu=len(stu_rol)
j=0
for j in range(nu):
    print('index',j,'=',stu_rol[j])

print('\n', " While with one")

k=0
while k < nu:
    print('index',k,'=',stu_rol[k])
    k+=1