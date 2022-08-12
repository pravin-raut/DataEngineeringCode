a=1
b=1
c=4

if(a>b):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)

mylist=[1,2,3,4,5,6,7,8,9,10]
print ("###################################")
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print("Odd Number {}".format(num))

mynewList=[(1,2),(3,4),(5,6),(7,8)]
print ("################Tuple Unpacking###################")

for a,b in mynewList:
    print(a)
    print(b)

print("################Dictionary###################")

mydict={'k1':1,'k2':2,'k3':3}

for i in mydict:
    print(i)

for i in mydict.items():
    print(i)

for key,values in mydict.items():
    print(key)
    print(values)

for values in mydict.values():
    print(values)

print("################While Loop###################")
x=0

while (x<5):
    print(f"The value of x is {x}")
    x=x+1
else:
    print(f"The value of x is {x}")
