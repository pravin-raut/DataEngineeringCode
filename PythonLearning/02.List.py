#1. List are ordered sequence that can hold  a variety of object type
#2. They use comma and [] to seprate object in list
#3. List support indexing and Slicing . List also support nesting
# Lists FAQ
#
# 1. How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
#
# You would just add another set of brackets for indexing the nested list, for example: my_list[2][1] . We'll discover later on more nested objects and you will be quizzed on them later!



my_list=[1,2,3,4,5]
my_list=[1,2,3,4,'Five']
print(my_list)
print(len(my_list))

print(my_list[4])

print(my_list[1:4])

anotherList=[6,'',7,8]

print(my_list+anotherList)

my_list[0]='NewEntry'
print(my_list)
print(my_list.append('NewAdded')) #to add item at end of list
print(my_list)
print(my_list.pop()) # to remove end item from list
print(my_list)

print(my_list.pop(0)) # to remove 0 item from list
print(my_list)
print(my_list.pop(-2)) # to remove  second last item from list
print(my_list)

newlist=['z','a','d','c']
numList=[4,1,0,4,-1,-6]
numList.sort() # this will sort and save it in the list itself
print(numList.sort()) #this is none type this will not retun anything,
print(numList)
print(numList.count(4)) #Count no of items in list
print(numList.index(4)) #Gives first occurence
print(sorted(numList))

newlist.sort()
print(newlist)



newlist.reverse()
print(newlist)