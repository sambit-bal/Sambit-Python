def pw(x,y):  # Actual Arguments
    z= x**y
    print(z)
pw(2,5)

def show(name,age):  #Keyword Arguments
    print(f"Name: {name} Age: {age}")
show(name="python" ,age=45)


def ard(name,age=23):  # Default Arguments
    print(f"Name: {name} Age: {age}")
ard(name="checkname")
ard(name="fullname",age=67)

def vla(x, *num): # Variable Length Argument
    z = x + num[0]+num[1]+num[2]
    print(z)
vla(8, 5,4,7)


def add(x, **num):   # keyword Variable Length Argument
    z = x+ num['a']+num['b']+num['c']
    print("Addition",z)

add(8,a=5, b=2, c=6)
