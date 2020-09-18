name = "HowToCheck"
old = "How"
new = "Python"
print(name)
str1 = name.replace(old,new) #replace funtion
print(str1)

name1 = "Hello-how-are-you"
str2 = name1.split('-') # split function
print(name1)
print(str2)

name3 = ('Hello', 'How', 'Are', 'You')
str3 =  '-'.join(name3) #join function 
print(str3)


name4 = "Hi How are You"
print(name4.startswith('Hi')) # startwith function
print(name4.endswith('You'))  # endwith function


