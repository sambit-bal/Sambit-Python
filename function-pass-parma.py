# Pass a Function as parameter

def disp(sh):
    #print(" Disp Function" + sh())
    return " Disp Function" + sh()

def show():
    return " Show Function"

print(disp(show))