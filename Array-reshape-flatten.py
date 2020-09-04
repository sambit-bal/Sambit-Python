from numpy import *

a = array ([10,20,30,40,50,60,70,80,90,100,110,120])
d = array ([10,20,30,40,50,60,70,80,90,100,110,120])

b = reshape (d,(2,6))  # one D to 2 D array
c= reshape (a,(2,3,2))  # One D to 3 D array
print(a)
print()
print(b)
print()
print(c)

print()
k = array([[10,20,30],[40,50,60]])
j = reshape(k,(6)) # 2 D to one D array
print(j)

# flatten method
print()
i = array([[10,20,30],[40,50,60]])
f=i.flatten()  # 2 D to One D array
print(f)