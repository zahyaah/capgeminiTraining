from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def profession(self):
        pass 

    def introduce(self):
        print(f"Hello, I'm a {self.profession()}")