import sys
print(sys.getrecursionlimit()) # defult run is 1000
sys.setrecursionlimit(50) # this will set to 50
i = 0
def myfun():
    global i
    i=i+1
    print("My function:", i)
    myfun()   # recursive function can run max 999 times

myfun()