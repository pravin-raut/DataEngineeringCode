def square(num):
    return num*num

list1=[1,2,3,4,5,6,7,8,9]
print(list(map(square,list1)))
print(list(map(lambda num:num**2,list1)))
def iseven(num):
    return num%2==0

print(list(filter(iseven,list1)))



#Global keyword will reassign the value


def CaseCheck(InputString):
    newlist=[i for i in InputString if i.strip()]
    #newlist2=list(map(lambda x: if x.isupper(): 'U' else: 'L',newlist))
    newlist3=[if i.isupper(): 'U' else: 'L'
                    for i in InputString]

    print(newlist3)
    
CaseCheck('pravin raut')