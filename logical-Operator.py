#logical and
a = 5
b = 2
c = 3
d = 20
e = 50
print( a > b and a > c)
print( a > b and a < c)
print( a < b and a > c)
print( a < b and a < c)

print ( a > b and d)
print( a > b and d and e)
print ( a < b and d )

#logical or

print ( a > b or b < c)
print ( a > b or b > c)
print ( a < b or b < c)
print ( a < b or b > c)
print( a < b or d)
print( a < b or d or e)

#logical not
print ( not (a < b))
print ( not (a > b))