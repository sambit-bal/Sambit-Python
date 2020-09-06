from numpy import *
m=int(input("Enter Number of Rows: "))
n=int(input("Enter Number of Column: "))

a = zeros((m,n),dtype=int)
u = len(a)

print(a)
print()
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Elements : "))
        a[i][j] = x

print()
for i in range(u):
    for j in range(len(a[i])):
        print("index",i,j,'=',a[i][j])

print()
print(a)

print(" Without Index")
i=0
for i in  a:
    for j in i:
        print(j)

