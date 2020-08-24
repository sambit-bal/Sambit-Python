# statement-nested-if else
a= int(input())
b= int(input())
c= int(input())
d= int(input())

if a > b:
    print(a," is greater than ", b)
    if c > d:
        print(a," is greater than ", b, "and", c," is greater than" , d, sep=" ")
    else:
        print(a, " is greater than ",b, "and", c ," is less than ",d , sep=" ")
else:
    print(a, " is less than ",b)
