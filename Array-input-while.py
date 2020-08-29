from array import *

stu_roll= array('i',[])
n = int(input("Enter number of Element : "))

i=0

while i < n:
    stu_roll.append(int(input("Enter number ")))
    i+=1

j= 0
while (j < len(stu_roll)):
    print(stu_roll[j])
    j+=1

print(stu_roll)