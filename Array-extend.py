# extend ()
from array import *

stu_sec1 = array ('i', [100,101,102,103,104])
stu_sec2 = array ('i', [105,106,107])

n = len(stu_sec1)
i = 0

while (i < n):
    print(stu_sec1[i])
    i+=1

print("After Array Extend")

stu_sec1.extend(stu_sec2)
n = len(stu_sec1)
i=0

while (i < n):
    print(stu_sec1[i])
    i+=1
