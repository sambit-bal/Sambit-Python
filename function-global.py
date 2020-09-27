a = 50  # global variable 

def show():  # keep a value as 50 and 10 
    a = 10  # local variable 
    print("Local variable A:", a)
    x = globals()['a']
    print("X:", x)
    x = 40
    print("X:", x)

show()
print("Global variable A:", a)