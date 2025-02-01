from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass