from Shape import Shape 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(3.14*self.radius*self.radius, 2)
