def disp():
    name = "Function test"
    print("Welcome to ",name)

disp()

# return multiple value
def calculate(y):
    x = 10
    c = x + y
    d = y - x
    return c, d

sum, sub = calculate(20)
print(sum)
print(sub)
