from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass 
    