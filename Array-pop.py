# POP in Array 

from array import *

stu_rol = array('i',[100,101,102,103,104])
n = len (stu_rol)
i=0
while (i <n):
    print(stu_rol[i])
    i+=1

print("Array after POP")

r = stu_rol.pop(3)  # stu_rol.pop()  will remove last value
n = len(stu_rol)
i=0

while (i < n):
    print(stu_rol[i])
    i+=1

print("Removed Element :" ,r)