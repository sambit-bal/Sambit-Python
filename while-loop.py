# While Loop

a = int(input())
print()
while a<=10 :
    print(a)
    a+=1
print("Print value less than 10")

# While loop with else

b = int(input())
print()
while b<=10:
    print(b)
    b+=1
else:
    print(" value is greater than 10")

print(" Great")


# Infinite while loop

c = int(input())
print()
while True:
    c+=1
    print(c)
    if(c == 5):
        break

print("Rest of the code")

# Nested While Loop

d = int(input())

print()

while d <= 3:
    print(" Outer Loop", d)
    d+=1
    e = 1
    while e <= 5:
        print("Inner Loop", e)
        e+=1
print("Rest of the code")
