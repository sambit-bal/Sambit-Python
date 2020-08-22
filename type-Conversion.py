# type-Conversion : implicit and explicit

## # type-Conversion : implicit 

a= 5
b= 2
value = (a/b)
print(value)
print(type(value))

d= "sambit"
e= "bal"
f= d + e
print(f)
print(type(f))

# type-Conversion :  explicit (type cast conversion)

w= 10
r= 8
value = w/r
print(type(value))
int_value=int(value)
print(int_value)
print(type(int_value))

o=20
p='10'
print(type(p))
l=o+int(p)
print(l)
print(type(l))

# string to Tuple

z="sambit"
vz= tuple(z)
print(vz)
print(type(vz))

lz=list(z)
print(lz)
print(type(lz))

s= 10
print(bin(s))
print(type(s))