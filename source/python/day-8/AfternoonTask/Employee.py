from abc import ABC, abstractmethod 

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass 

    @abstractmethod
    def getSalary(self):
        pass 

