# numpy one D array syntax for arange
# syntax : numpy.arange( start, stop, stepsize, dtype=None)

from numpy import *
#stu_rol= arange(5)
#stu_rol= arange(1,6)
#stu_rol= arange(1,10,2)
stu_rol= arange(1, 10, 2)
nu =len(stu_rol)

for k in stu_rol:
    print(k)

print('\n', " For with arange")

for i in range(nu):
    print('index',i,'=',stu_rol[i])
    
print('\n', " While with arange")
j=0
while (j < nu):
    print('index',j,'=',stu_rol[j])
    j+=1
    