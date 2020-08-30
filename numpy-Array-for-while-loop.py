from numpy import *

stu_rol = array([100,101,102,103,104])

n= len(stu_rol)
i =0

# for lopp with range
print('\n' "For Loop")
for i in range(n):
    print(stu_rol[i])
    i+=1


# for lopp with array
print('\n' "For loop with Array")
for j in stu_rol:
    print(j)

# while loop
print('\n' "While function ")
i=0
while (i < n):
    print('index', i, "=", stu_rol[i])
    i+=1