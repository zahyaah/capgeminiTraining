from Shape import Shape 

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length 
        self.breadth = breadth 
    
    def area(self):
        return self.length*self.breadth 