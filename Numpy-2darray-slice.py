from numpy import *

a = array([[10,20,30],
            [40,50,60],
            [70,80,90]])

print(" Original Array :")
print(a)

print(" Array value over ROW:")
n = a[0, :]
print(n)
print(" Array value over Column:")
m =a[:, 0]
print(m)
print("Array value over row and column:")

o = a[0:2,1:3]  # row start with 0 and end with 1 , cloum start with 1 and end with 2
print(o)
print()
print(a[0:2,0:2])