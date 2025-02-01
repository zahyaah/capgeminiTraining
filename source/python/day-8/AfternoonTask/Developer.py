from Employee import Employee

class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
    
    def work(self) -> str:
        return f"{self.name} is developing, debugging and innovating."
    
    def getSalary(self) -> int:
        return self.salary