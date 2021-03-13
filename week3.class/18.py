class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.lname,self.fname)
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.gy=2020
x=Student("Kyran","Yerkin")
print(x.gy)