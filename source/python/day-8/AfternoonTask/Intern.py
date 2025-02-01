from abc import ABC, abstractmethod
from Employee import Employee

class Intern(Employee):
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is learning and assisting"

    def getSalary(self) -> int:
        return self.salary;
