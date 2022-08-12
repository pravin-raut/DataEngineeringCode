from random import *

mylist=[1,2,3]

for x in mylist:
    pass

myname='Pravin'
for x in myname:
    if x=='a':
        continue
    print(x)
print("End")

x=0
while (x<5):
    print(f"The value of x is {x}")
    x=x+1
    if (x==2):
        break
else:
    print(f"The value of x is {x}")


print("############Range1#############")

for i in range(1,10,3):
    print(i)
print("############Range2#############")

for i in range(5,10):
    print(i)

name="Pravin Raut"

for index,char in enumerate(name):
    print(index)
    print(char)

mylist1=[1,2,3,4,5,6]
shuffle(mylist1)
print(mylist1)
mylist2=['a','b','c']

for items in zip(mylist1,mylist2):
    print(items)

print(1 in [1,2,3])

print('a' in 'pravin')

print(min([1,2,3]))
print(max([1,2,3]))
mylist3=[1,2,3,4,5,6]
shuffle(mylist3)
print(mylist3)

print(randint(10,100))
#a=input("Enter input")
#print(a)

print("##########List Compreshension###########")

newlist= [x for x in 'PRAVIN']
print(newlist)

newlist= [x+2 for x in range(0,10) if x%2==0]
print(newlist)

for num in range(1,101):
    if(num%3==0) and (num%5==0):
        print("FB")
    elif (num%3==0):
        print("F")
    elif (num % 5 == 0):
        print("B")
    else:
        print(num)

help(newlist.insert)

