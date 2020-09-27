addd = lambda x,y :x+y
print(addd(2,5))

value_check = lambda x,y :(x+y, x-y)  # lambda function
print(value_check(10,6))
#***********************************************************************
add = lambda x = 10 : (lambda y : x + y ) # Nested lambda function
a = add()
print(a)
print(a(20))

#***********************************************************************

def show(a):               # Passing Lambda Function to another Function
    print(a(10))

show (lambda x : x)

#***********************************************************************

def ladd():               # Returning  Lambda Function from  another 
    p = 20
    return (lambda g : g + p )

u = ladd()
print(u(20))

#***********************************************************************

(lambda x : print(x + 1))(5)  # IIFE  Lambda Function ,not recomanded to use 

