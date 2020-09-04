from numpy import *

a = array ([ [10,20,30],
             [40,50,60]])

# Without Index
for r in a:
    for c in r:
        print(c)
    print()

# With Index
n = len(a)

for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()