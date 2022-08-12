Location="C:\\Users\\Dell\\OneDrive\\Pravin\\PythonLearning\\InputFiles\\Input.txt"

myfile=open(Location)
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

myLines=myfile.readline() #First Line
print(myLines)

myLines=myfile.readlines() #Read all line in list
print(myLines)

myfile.close() #CLose the file

#when you do this you dont have to worry about closing the file

with open(Location) as Mynewfile:
    content=Mynewfile.read()

print(content)
writeLocation="C:\\Users\\Dell\\OneDrive\\Pravin\\PythonLearning\\InputFiles\\Output.txt"

with open(writeLocation,mode='w') as Mynewfile:
    Mynewfile.write("Pravin Raut")
    # mode =r --> Read only
    # mode =w --> Write only/Overwrite
    # mode =a --> Append only
    # mode =r+ --> Reading & Writing
    # mode =w+ --> Writing and Reading (Overwrite existing file)