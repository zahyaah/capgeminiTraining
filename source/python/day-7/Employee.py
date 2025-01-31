from Work import Work

class Employee: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age 

    def toString(self):
        return self.name + " is " + str(self.age) + " years old."
    

firstEmp = Employee("Zayd", 12) 
print(firstEmp.getAge())
print(firstEmp.getName())
print(firstEmp.toString()) 

someWorkObject = Work()