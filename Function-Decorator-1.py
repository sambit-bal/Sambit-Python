def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi
    return inner

def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner
@decor
@decor1
def num():
    return 10
# num = decor(decor1(num)) # this can written on line 14 and 15
print(num())