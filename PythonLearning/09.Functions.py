workhours=[('A',100),('b',2000),('c',400)]

for i,j in workhours:
    print(i)
    print(j)

def Checkworker(tyupleinput):
    name=''
    hours=0
    for i, j in tyupleinput:
        if j>=hours:
            hours=j
            name=i
        else:
            pass
    return (name,hours)

a=Checkworker(workhours)
print(a)
name,hours=Checkworker(workhours)

print("Name is {} and Hours are {}".format(name,hours))
#args can be of any name * is mandatory -its internally create a tupe
def funct(*args):
    return sum(args)

a=funct(1,2,4)
print(a)
#kargs can be of any name ** is mandatory -its internally create a dictionary

def funct1(**kwargs):
    if 'Maths' in kwargs:
        print("In Maths I got {} Marks".format(kwargs['Maths']))
    else:
        print('Nothing found')

funct1(Maths='90')


def combined(*args,**kwargs):
    print(args)
    print(kwargs)
    print("HI check this no 1 is {} and no 2 is {}".format(args[1],kwargs['fruit']))

combined(1,2,3,4,fruit='Mango')


def functionword(word):
    listofword=word.split()
    print(listofword)
    if(listofword[0][0]==listofword[1][0]):
        return True
    else:
        return False

print(functionword('Pravin Raut'))

def reverseword(word):
    listofword = word.split()
    reversewordlist=listofword[::-1]
    StringSent=' '.join(reversewordlist)
    return StringSent

print("################")
print(reverseword('Pravin Raut'))

list1=[1,2,3,6,4,7,8,9,10]
print(list1.index(6))
Newlist1=list1[0:list1.index(6)]
Newlist2=list1[list1.index(9)+1:]
print(Newlist1+Newlist2)


def spygame(nums):

    templist=[0,0,7,'x']
    for i in nums:
        if (i==templist[0]):
            templist.pop(0)
        else:
            pass
    return len(templist)==1
list1=[1,2,32,4,42,0,0,123,7]
print("################")

print(spygame(list1))
