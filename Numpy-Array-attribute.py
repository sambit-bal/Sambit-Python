from numpy import *

a = array ([10,20,30,40,50])
b = array ([[100,200,300],[400,500,600]])
print()
#array dimention like 1D or 2D
print("1D Array ndim:",a.ndim) 
print("2D Array ndim:",b.ndim)
print()

print("1D Array shape",a.shape) # Array shape like how many iteam in 1 D array
print("2D Array shape",b.shape) # Array shape like how many 2 D (2,3)
print()

print("1D Array size",a.size) # total element like 5
print("2D Array size",b.size) #total element like 6
print()

print("1D Array itemsize",a.itemsize) # Memory size of that array like 4
print("2D Array itemsize",b.itemsize) # Memory size of that array like 4
print()

print("1D Array dtype",a.dtype)  # data type like int
print("2D Array dtype",b.dtype)
print()

print("1D Array nbytes:",a.nbytes) # total byte on array like 20
print("2D Array nbytes:",b.nbytes) # total byte on array like 24