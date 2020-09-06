from numpy import *
m = int(input("Enter Row for the Array : "))
n = int(input(" Enter Column for the Array: "))

a= zeros((m,n),dtype=int)
print(a)
u = len(a)
i =0
while i < u:
    j=0
    while j < len(a[i]):
        x = int(input("Enter Array element : "))
        a[i][j] = x
        j+=1
    i+=1

i = 0 
while i < u :
    j=0
    while j < len(a[i]):
        print('index',i,j,"=",a[i][j])
        j+=1
    i+=1

print(a)

