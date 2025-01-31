from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def about(self):
        pass 

class Son(Father):
    def about(self):
        print("I'm the Son")

class Daughter(Father):
    def about(self):
        print("I'm the Daughter")



S = Son() 
S.about()

D = Daughter()
D.about()