from abc import ABC, abstractmethod
from Employee import Employee 

class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def getSalary(self) -> int:
        return self.salary; 

    def work(self) -> str:
        return f"{self.name} is managing developers."
    
    
