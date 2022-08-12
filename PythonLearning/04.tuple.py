#Tuples are very much similar to list . However they have one key diffrence immutablity
#Once an element is inside stirng they cannot be reassigned
#immutable=Cannot change

a=(1,2,3,5,0,1)

print(a.count(1)) #Gives no of occurence
print(a.index(1)) #Gives first occurence
print(a[0:3])

#a[0]=5 #TypeError: 'tuple' object does not support item assignment
