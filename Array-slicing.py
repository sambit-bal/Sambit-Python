# Slicing array 

from array import *

stu_rol = array('i', [100,101,102,103,104,105,106,107,108])
print("origianl array")
n = len(stu_rol)

for i in range(n):
    print(i, "=", stu_rol[i])

print("************************")

a = stu_rol[0:7:2]  # stu_rol[0:], stu_rol[-2:],stu_rol[:-2], stu_rol[0:7:2]
for i in a:
    print(i)

