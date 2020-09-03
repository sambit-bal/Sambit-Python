from numpy import *

a = array([100,20,30,200,400])
b = array([25,120,130,28,44])

result = where (a > b, a , b)

print(result)