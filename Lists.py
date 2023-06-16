'''
if we don't want to end line after print() use **end** method in it
it specifies what to do after printing all those
by default it is '\n' so end line'''
print(2,3,4,5,end = " ") #will give a space after this print
print(1,2)

l=[] #daclaration
list1=[1,2,3,4,"hjvj",'s']
print(id(list1))
list1.append(22)
print(id(list1)) # as id didn't change after changing list so list is a mutable object
string1="sdf"
print(id(string1))
string1+="k"
print(id(string1))  #here id changes so string is immutable in string it creates a new s variable and assign it as previous s + "k"

print("\nslicing \n")
#slicing  same in string
print(list1[4]) #print value at index 4
print(list1[4:]) #print value after 4
print(list1[1:4]) #print value from index 1(inclusive) to index 4(exclusive)
print(list1[:4]) #print upto index 4(exclusive)
print(list1[1:5:2]) #print with a jump of 2 indexes from [1,5)
print(list1[5:1:-1]) #print reversaly from [5,1)
print(list1[::-1]) #print full list in reverse order

list1[4:] = []  #delete all elements after index 4(including)
print(list1)
list1[0]=[2,8,True]  #replacing first element by list
print(list1[0][2])  #sublists

#Unpacking
## directly putting in variable
print("Unpacking")
list_ = [2,4,3]
a,b,c = list_  #should have equal no. of variables
print(a,b,c)  #also in tuple

print("\nother functions\n")
#some other functions
print(len(list1))  #list length (same for string)
list1.insert(2,"skc") #to insert at index 2 (append only at last)
print(list1)
list1.pop() # to remove last element
list1.pop(3) # to remove at index 3 
tuple1 = (4,3,67,2)  # tuple () brackets
list2 = [3,2,5,2]
set1 = {2,6,89}  #if key pair wise used then dictionary else set
list1.extend(tuple1)   #extend merge list with tuple, list , set, string.....
list1.extend(list2)
list1.extend(set1)
print(list1)
list1.extend("ppsfspp") #merge string -> add each character (treats string as list of character)
print(list1)
list2 = [1,8,2,4,0,5,3]
list2.sort()  #to sort list
print(list2)
print(max(list2)) # maximum element in list ( also min function)


### mutable and immutable data
print("\nmutable and immutable data\n")
a=5
b=5
c=5
d=4
print(id(a))
print(id(b))
print(id(c))
print(id(d))
d+=1
print(id(d))
# if **integer** value same then only one copy of that data in list and that varible points towards that data
#id gives memory address if stored block 
#so 5 <- a,b,c,d(4+1)
string2 = string1 #copying gives same address as copying whole string
string3 = string1[:] #another way to copy
print(id(string1))
print(id(string2))
print(id(string3)) 
print(string1)
string4 = "sdfk"
print(id(string4))
string4+="k"
print(id(string4))
print(string4)
string4 = string1[0:3]
string4 += string1[3]
print(id(string4))

#List Comprehension
#syntax
## a = [x for x in (another list/range..) if(optional)]
print("\nList Comprehension \n")
a = [1,3,2,5,7]
b = [x for x in a if x%2==1]  #1 liner loop/condition to initialise list
print(b)
c = [x**3 for x in b]
b = [x**3 if(x%2==0) else x**2 for x in range(0,6)]  # if we want to use if else then use if before loop
print(c)
print(b)

#tuples
#immutable else same as list
#immutable so no append,insert,pop... functions
print("\ntuples\n")
t = (2,4,6)
print(type(a))
#list in tuple
a = (1,2,3,[4,2,5])
a[-1].append(1)
print(a)
## list changed
## tuples , lists, stores references/location of elements
# so in tuples these references can't be changed
# but there exists a list and it's reference can be changed so we can add an element in list
# but our tuple is still referring to that list only(now to changed) and reference didn't changed
#list changed but it's location didn't
import sys  #importing/using modules/other pythonfiles
print(sys.getsizeof(a)) 
a[-1].extend([x for x in range(1000)])
print(sys.getsizeof(a))
#so sizeof tuple depends on reference not on size of reference
#size of tuple = 40 + 8* no.of elements
a=(1)
print(type(a))  # it will be treated as a simple integer
a=(1,)
print(type(a)) #for one element tuple use a comma also with it

#typecasting of tuples and lists
print("\ntypecasting\n")
a = (1,2,3,4)
print(type(a))
a= list(a)
print(type(a))
a=tuple(a)
print(type(a))



