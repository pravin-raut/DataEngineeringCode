# Strings FAQ
# 1. Are strings mutable?
# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
# 2. How do I create comments in my code?
# You can use the hashtag # to create comments in your code


Name="Pravin Raut"

#printing Length
print(len(Name)) #Length of string

#Slicing String
print(Name[0]) # output is P
print(Name[7:]) #output is Raut
print(Name[-1:]) #output is t , to start from reverse
print(Name[0:3]) #output is Pra
print(Name[0:3:1]) #output is Pra
print(Name[0::2]) #output is Pai at
print(Name[::-1]) #Reverse


#New Line Character
print ("Hello \n world")
print ("Hello \\n world")

#Immutablity of String

#Name[0]='S' THis will give error as string asssignment is not possible
#how to do it then
LastLetters=Name[1:]
print('S'+LastLetters) #Concat can be done with +

x="Good Morning"
x=x+" Hello"
print(x) #String Concatention and assignement
print(x*10) #String Repeating after Multiplication

print(2+3) #Output 5

print('2'+'3') #Output 23

#print('2'+3) #TypeError: can only concatenate str (not "int") to str

#Using of Method
print(Name.upper()) #Output PRAVIN RAUT

print(Name.upper) #Output <built-in method upper of str object at 0x0000020CE9E34130>

#Splitting String to List
SplitName=Name.split()
print(SplitName)

SplitName=Name.split('a')
print(SplitName)

print(type(SplitName)) #<class 'list'>

#String Interpolation
print("THis is a string {}".format("Inserted")) #Output :THis is a string Inserted

print("THis is a string {} {}".format("Inserted1","INserted2")) #Output :THis is a string Inserted1 INserted2

print("This is {2} {0} {1}".format("a","b","c")) #Output :This is c a b

print("This is {b1} {a1} {c1}".format(a1="a",b1="b",c1="c")) #Output :This is b a c

#Float Formation
result=100/77
print("The result was {r:10.3f}".format(r=result)) #ouptut The result was      1.299

print("The result was {r:1.3f}".format(r=result)) #ouptut The result was 1.299


#New method from Python 3.6
name='Pravin'
print(f"Name is {name}") # Output is Name is Pravin


#For Formmating https://pyformat.info/


#Find Square root

print(144**0.5)

#Square

print(12**2)