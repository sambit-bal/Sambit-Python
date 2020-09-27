# Global keyword

a = 20
b = 30

def show():
    a  = 10
    global b   # how to keep global value inside function 
    print("A:", a)
    print("B:", b)

show()
print("A",a)
