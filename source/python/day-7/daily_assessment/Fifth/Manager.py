from Person import Person
from Employee import Employee

class Manager(Person, Employee):
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
    
    def get_name(self):
        return self.name 
    
    def get_salary(self):
        return self.salary 


