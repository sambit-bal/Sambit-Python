from numpy import *

# zero () function on 2 D array

a = zeros((3,2),dtype=int)
print(a)
print()

# for loop without index
for r in a:
    for c in r:
        print(c)

# for loop with index
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print('index',i, j, '=', a[i][j])
    print()

# while loop with index
i=0
while i < n:
    j = 0
    while j < len(a[i]):
        print('index',i,j,'=',a[i][j])
        j+=1
    i+=1
    print()


