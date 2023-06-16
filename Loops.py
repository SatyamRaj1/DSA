# While loop

x=5
while(x>0):   # can also be "while x>0: "
    print(x)
    x-=1

print()
#for loop
l = [[3,7,9],1,2,3,4,5,6]
for x in l:   #iterate in arr using x as iterator
    print(x,id(x))   #similar for string, each iterator points to -> char
print(id(l[0]))  #above x was referring to same element not a copy

print()
#range function
for i in range(1,3):  #from 1 to 3(not included)
    print(i)
print()
for i in range(4):  #no start vlue given so from 0 to 10
    print(i)

# range(start, end, step_size) 
# by default start=0 , step_size = 1  *end -> not included)
print()
#Continue and Break
#continue -> goes to next iteration skipping remaining code of current iteration
#break -> terminate iteration (current loop) completely t the instant it is encountered
for i in range(1,10):
    print(i)
    if(i==2):
        continue
    if(i==2 or i==4):
        break
    print("b")


#  **** for loop and while loops have generally same speeds but python has optimized for loops
#  so in **Python** for loop is faster

#tuples
