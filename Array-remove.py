from array import *

stu_rol= array('i',[100,101,102,103,104])
n = len(stu_rol)
i=0

while(i < n):
    print(stu_rol[i])
    i+=1

print("After Array remove ")

stu_rol.remove(102)
n= len(stu_rol)
i=0
while(i < n):
    print(stu_rol[i])
    i+=1
    