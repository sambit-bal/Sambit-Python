from array import *

stu_roll = array('i',[100,101,102,103,104,105])

n = len(stu_roll)
r = 0

while r < n:
    print(stu_roll[r])
    r+=1

print("Append Array value")

stu_roll.append(106)
n = len(stu_roll)
r = 0

while r < n:
    print(stu_roll[r])
    r+=1