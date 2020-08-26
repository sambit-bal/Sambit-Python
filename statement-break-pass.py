# # Break Statement

for i in range(10):
    if (i == 5):
        break
    print(i)
print("Rest of the code")

# # Continue Statement

for i in range(10):
    if (i == 5):
        continue
    print(i)
print("Rest of the code")

# Pass Statement

a = int(input())
b = int(input())

if a > b:
    pass
else:
    print(a,"is not greater than",b)

print(a, "is greater than ", b)

i = int(input())
print()
while i <= 10:
    if (i == 5):
        pass
    print(i)
    i+=1
print("Rest of the code ")