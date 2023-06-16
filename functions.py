#syntax:  def {$function_name}({$arguements}):
def func(a,b): #a,b parameters (input to function)
    if(a%2 == 1):  
        return a+b  #optional
    else:
        return a-b
print(func(3,4))
a = func(6,5)
print(a)

## Parameters v/s Arguements
# def func(a,b) here a,b are paramenters
#values we pass in parameter are arguements
#a = func(a,b) a,b are arguements(at time of call)
# so we pass arguements in parameters

#passing arguements by naming
b = 3
a = 4
print("naming arguements")
print(func(3,4))  #if we directly give arguements then it is one to one mapping 
print(func(b=3,a=4))#but if we give name in function then mapping is from name
print(b,a)
print(func(b,a)) #naming in function only so b maps to a
print(func(a,b))

#default parameters
# if arguement not given then it these are used by default
print("default parameter")
def f1(a,b=3,c=4):  #default parameter can't be given before non default parameter
    print(a,b,c)     #f1(a=4,b,c=3) not allowed
f1(2)
f1(2,1) #2 arguements is given so uses last default parameter only
f1(2,1,0)

###only in python we can return multiple values
def f2():
    return 2,4,6
a,b,c = f2()
print(a,b,c)
print(f2())  #returns as a tuple and can be stored in individual or tuple
a = f2()
print(a)

a = (4,3)
b,c = a
print(b,c)

### *** if __name__ == "__main__"" function
print('\n if __name__ == "__main__"" \n')
## like main() function of c++
# if we write all things in functions then first invoking function is this
# via this function we can call all functions
# it is called directly
# so when we run a file it sets a internal attribute __name__ to "main"
#use
'''when we imprt a file if commands are written outside (not in main) then they
will be executed
but commands inside main doesn't get executed
without running __nme is set to be name of file so doesn't get executed
'''
import function_helper
## here lines outside main are executed but not inside
## if we run function_helper.py we will get both outside and inside main lines executed
''' so if we have some functions inside other files we can use them via import
without running the whole python'''
#if we write some code in else then it will be executed while importing not running

print("\nscope\n")
## Scope
a = 10
def f3(): #both a are different(inside and outside one
    #print(a)  will give error as we are assigning a loval variable a after it
    a=5  #here a is a local variable so it' s value is 5 but changing here won't change it's global value
    print(a) #also ifwe had passed as an arguement then also a copy would have been passed so original value won't be changed
def f4():
    print(a) #here we are not declaring any local variable with name a so it will take gobal variable
f3()
f4()
print(a)
''' we can't change reference of gobal variabe in a function
so if we do print(a), b = a+5 then no problem
when we do a=5 then it will make another 'a' (local)
but if we do like b=a+5 and then a = 5 then in b=a+5 global 'a' is used then
in function we got 'a' global variable so can't change it
for list if a = [2,4]
then we can't perform a = [4,6] after printing/using global but we can use append
as we are not changing reference of 'a' but append/insert doesn't change reference
to change reference we have to use global keyword
'''
def f5():
    global a
    print(a) 
    a=5  #here value of global variable changed so will be reflected outside too
    print(a)
f5()
print(a)

print("\nsome inbuilt functions \n")
print("split()\n")
#split function
#used to split a string on basis of a symbol/string
#mostly usedto slip by space(by default but can be used to split date of dd-mm-yyyy format by '-'
s = "i am too much lazy"
a = s.split()
print(s,'\n',a)
#for other symbols mention them as arguement
a = s.split('m')
print(a)
# we can limit no. of divisions by mentioning it
a = s.split(" ",3)
print(a)
#if we try to cut by a character which isn't present then no change

print("\njoin()\n")
#Join
#opposite of split
#joins list in string
#joins by string given before (put that between list elements) if none required use ""
s = "-".join(a) 
print(s)
## Much faster than joining with loops

print("\nmap() syntax : map(function,list)\n")
#map syntax : map(function, list)
# just iterate through collections and apply a fuction to every object of collection
print(list(map(int,["12","14","34"],)))
#return a map object so need to convert again to datatype(mostly list)
def f6(x):
    return x**4
print(list(map(f6,[1,2,3,4]))) #similiar to [f6(x) for x in [1,2,3,4]]
#same as list comprehension
'''x = list(map(int,input().split())) #to take many integers as input separated with space in 1 line
print(x)
'''
print("\nreduce()\n")
'''takes 1 arguement(initially first element of list then take another and
perform function (given) with both then again take another value and perform
function with previous result and value and again so on..
'''
import functools
print("sum = ",functools.reduce(lambda a,b:a+b,[1,2,3,4,5]))
print("max = ",functools.reduce(lambda a,b:a if a>b else b,[1,2,6,3,4,5]))





