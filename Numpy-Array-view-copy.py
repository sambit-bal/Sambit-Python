from numpy import *
# view method
a = array ([100,200,300,400,500])
b = a.view ()
b[1] =80
print(a)
print(b)

print("a", id (a))
print("b",id(b))

# copy method

d = array([100,200,300,400,500,600])
e =copy(d)

d[1] =80
e[2]=22
print(d)
print(e)

print("d",id(d))
print("e",id(e))