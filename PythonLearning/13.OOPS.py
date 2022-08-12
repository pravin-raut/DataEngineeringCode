class Calculator():
    #Class Object Attribute
    #same for any class
    Name_Of_Calculator="Pravins Calculator"

    def __init__(self, no1, no2):
        #Attribute
        #take the arguments
        #assign it using self.attributename
         self.no1 = no1
         self.no2 =no2

    def add(self):
        print(self.no1+self.no2)
        return self.no1+self.no2


myCalc=Calculator(2,3)
myCalc.add()


class Circle():

    #Class level object attributes
    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area =self.radius*self.radius*Circle.pi

    def get_Circumference(self):
        return self.radius*self.pi*2

mycircle=Circle(5)
print(mycircle.area)
a=mycircle.get_Circumference()
print(a)