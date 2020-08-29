from array import *

stu_roll = array('i', [])
n = int(input("Enter number of Elements: "))


for i in range(n):
    stu_roll.append(int(input ("Enter Number : ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])

print(stu_roll)