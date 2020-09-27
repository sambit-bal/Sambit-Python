# Pass or Call by Object Reference 

#Case-1
def show(x):
    x = 15
    print(x, id(x))  # ID value different with integer object and two object created ,interger object's are immutable

x = 10
show(x)
print(x, id(x))
print()
#Case-2
def val(lst):
    print("IFBA", lst,id(lst))  #inside function before append
    lst.append(4)
    print("IFAA:", lst, id(lst))  #inside function after append
   # ID value same object value for list  ,list object's are mutable 
lst = [1,2,3]
print("BCF:", lst, id(lst))  #Before calling function 
val(lst)
print("ACF:", lst, id(lst))  #After calling function 

# Immutable Object :  Interger , Float, String and Tuple
# Mutable Object :  List, Dictonary 

#Case-3
print()
def vall(lstt):
    print("IFBA", lstt,id(lstt))  #inside function before append
    lstt = [11,22,33]
    print("IFAA", lstt,id(lst))  #inside function After append

lstt = [3,4,5]
print("BCF:", lstt, id(lstt))  #Before calling function
vall(lstt)
print("ACF:", lstt, id(lstt))  #After calling function