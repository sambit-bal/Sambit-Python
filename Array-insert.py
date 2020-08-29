# Insert 

from array import *

stu_rol = array('i',[100,102,103,104,105,106,107])
n = len(stu_rol)

i = 0

while (i < n):
    print(stu_rol[i])
    i+=1

print(" Array after insert")
stu_rol.insert(1,108)
stu_rol.insert(4,180)

n = len(stu_rol)
i= 0

while (i < n):
    print(stu_rol[i])
    i+=1

