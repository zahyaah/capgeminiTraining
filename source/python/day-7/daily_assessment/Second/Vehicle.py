from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand 
    
    @abstractmethod
    def max_speed(self):
        pass 