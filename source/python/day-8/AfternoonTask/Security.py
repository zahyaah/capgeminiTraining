from Employee import Employee

class Security(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self) -> str:
        return f"{self.name} is guarding the place."
    
    def getSalary(self) -> int:
        return self.salary