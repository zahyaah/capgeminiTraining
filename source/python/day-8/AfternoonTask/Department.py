from Employee import Employee

class Department: 
    def __init__(self, name: str):
        self.name = name 
        self.employees = []
    
    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")
    
    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")
    
    def getTotalSalary(self) -> int:
        return sum(employee.getSalary() for employee in self.employees) 
    
    def showEmployeeDetails(self) -> None:
        for employee in self.employees:
            print(f"{employee.name}\t{employee.getSalary()}\t{employee.work()}")
    