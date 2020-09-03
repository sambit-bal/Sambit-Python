from numpy import *

n = int(input("Enter Number of Elements: "))
a = zeros(n,dtype=int)

for i in range(len(a)):
    c=int(input("Enter Elements: "))
    a[i] = c
    
print(a)