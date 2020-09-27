# Local variable and Global variable 
a = 30  # global variable 
#c = 0
def show(y):
    x = 10   # local variable
 #   c = 0
 #   c = c+1
    print("Local Variable : ",x)
    print(a)
    print(x + y)
    
show(5)

#print ("x:",x)
print("Global Variable :", a)
