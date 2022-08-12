# 1. Dictionaries are unordered mappings for storing object .Dictornaries uses key value pair instead.None
# 2.THis key value pair allows user to quickly grab object without needing to know an index location
# 3. Dictionary uses curly braces and colons to signify the key and associated values
# {key1: value1,key2:value2}
# 4.When to use list vs dictionary
# Dictionary:
#     1. Object retrived by key name
#     2. unorderd and cannot be sorted
# List:
#     1. Objects are retrived by location
#     2. Ordered sequence can be indexed or sliced.
#
# Dictionaries FAQ
#
# 1. Do dictionaries keep an order? How do I print the values of the dictionary in order?
#
# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object lecture later on in the course!
#



Mydict={'Name':'Pravin','age':32}
print(Mydict['Name']) #Output is Pravin




Mydict={'Name':'Pravin','age':32,'Name':'Pravin1'}
print(Mydict['Name']) #Output is Pravin1


print(Mydict.keys()) #Retun all keys
print(type(Mydict.keys())) #<class 'dict_keys'>

print(Mydict.values()) #Retun all keys
print(type(Mydict.values())) #<class 'dict_keys'>

print(Mydict.items()) #Retun all keys
print(type(Mydict.items())) #<class 'dict_keys'>

Mydict['Name']='Pravin Raut'
print(Mydict['Name']) #Output is Pravin Raut


NestedDict={'One':[1,2,3],'Two':{'two.one':21}}

print(NestedDict['One'][0])
print(NestedDict['Two']['two.one'])

