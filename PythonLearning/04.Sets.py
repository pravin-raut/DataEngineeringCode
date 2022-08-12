# 1. Sets are unordered collection of unique elements

myset=set()
myset.add(1)

print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset) #Nothing will add

Mylist=[1,2,2,2,4,5,5,6,1]
print(set(Mylist))


a='Mississippi'
Mulist=set(list(a))
print(Mulist)