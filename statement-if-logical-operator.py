# if with logical operator
if((5 > 4) and (3 < 8)):
    print("All value are great")
print("Rest of the code")

if((5 < 4) and (3 < 8)):
    print("All value are great")
print("Rest of the code for false")

if((5 < 4) and (3 > 8)):
    print("All value are great")
print("Rest of the code both false")

if((5 < 4) and (3 > 8)):
    print("All value are great")
print("Rest of the code right false")

if((5 > 4) or (3 > 8)):
    print("All value are great for or") # this should run
print("Rest of the code both false")