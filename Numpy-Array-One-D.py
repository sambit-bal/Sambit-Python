# numpy with array function 
# numpy one D array syntax 
# syntax : numpy.array( object, dtype= None, copy=True, order='k', subok=False, ndmin=0)
from  numpy import *
#import numpy

stu_rol = array([100,102,103,104,105],int)
stu_name = array(["ram", "shiba","durga","lakshim","ganesh"],dtype=str)

n = len(stu_rol)
i=0
while (i < n):
    print(stu_rol[i])
    i+=1
print()
l = len(stu_name)
i = 0

while(i < l):
    print(stu_name[i])
    i+=1

stu_rol[1] = 109
print()
print(stu_name[2])
print(stu_rol[1])
print()

print(stu_rol.dtype)
print(stu_name.dtype)  # Maxim char from that name ,like lakshim