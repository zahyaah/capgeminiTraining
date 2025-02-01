from Department import Department
from Developer import Developer
from Intern import Intern
from Manager import Manager

dev1 = Developer("Zayd", 1000000) 
intern1 = Intern("Dean", 1020312031)
manager1 = Manager("Sam", 530000)

department1 = Department("R&D")
department1.hire(dev1)
department1.hire(intern1)
department1.hire(manager1)

department1.showEmployeeDetails()