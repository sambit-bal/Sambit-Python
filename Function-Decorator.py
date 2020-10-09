def decor(fun):
    def inner():
        print("IF: Before enhancing Function")
        fun()
        print("IF: After enhancing Function")
    return inner

def num():
    print("We will use this function")
    print("and will enhance this in decorator")

result_fun = decor(num)
print(result_fun)
result_fun()