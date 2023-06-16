from operator import truediv     #to include/use another module/file
from pickle import FALSE


a = True
b = True
if(a):   # no bracket in python semicolon(compulsory)
    print("a")  #to define block we use indentation
    b=a  #here b=a is in if block
c=False #c is not in if block
a=False
if(a):
    print("d")
elif(b):  #elif = else if -> if is not true of above then check condition
    print("b")  


if(a):
    print("p")
else:
    print("t") #if previous a is not true then this block


if(a):
    print("ts")
elif(c):
    print("c")
else:   # if neither if nor elif are true
    print("q")



#Conditions
print(bool(0.001)) # if 0,False,[],(),"" (empty list,tuple,set,dictionary,string) , None(null in python)    are in bool then false else true
print(bool(()))
print(bool({}))
print(bool(""))
print(bool(None))

#relational operators
#comparing operators  == , > , >= , <= , !=(not equal )
print(2!=3)

#in Keyword
#to check if element is present in a list,tuple,set
#also to check if character/ string is present in other string
print("in keyword")
print(2 in [1,3,4,6])
print(1 in [1,3,4,6])
print("sd" in [2,5, 31,5,2,"sdgd"])
print("sd" in [2,5, 31,5,2,"sd"])
print("sd" in "sdgdfh")
print("sd" in "dfgsdfg")

#is keyword
print("is keyword")
x=4
y=4
print(x is y)
print(x==y)
x=[1,2,3]
y=[1,2,3]
print(x is y)  #checks if both have same id(can also help in mutability)
print(x==y)

#logical operator
# and,or,not
print("logical operator")
a=True
print(not(a))
print(not a)
b=False
print(a and b)
print(a or b)
print(a and (b or True))

