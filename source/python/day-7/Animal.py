from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Concrete method it is.")