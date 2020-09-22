# Nested Function 

def disp():
    def show():
        print("Show Child Function")
    print("Master Function")
    show()
disp()

def dispp(st):
    def showw():
        return " Show Child Function"
    result = showw() + st + " Dispp Function"
    return result

print(dispp(" showfunction "))