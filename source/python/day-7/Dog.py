from Animal import Animal 

class Dog(Animal):
    def sound(self):
        print("Dog- Woof~")

dog = Dog() 
dog.sound()