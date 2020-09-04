from numpy import *

a = ones((3,2),dtype=int)

print(a)

# for without index

for r in a:
    for c in r:
        print(c)
    print()

# for with index

n =len(a)

for i in range(n):
    for j in range(len(a[i])):
        print('index',i,j,'=', a[i][j])
    print()

# while with index
k=0
while  k < n:
    l=0
    while l < len(a[k]):
        print('index',k,l,'=',a[k][l])
        l+=1
    print()
    k+=1
