from Animal import Animal 

class Cat(Animal):
    def sound(self):
        print("Cat: Meow~")


cat = Cat() 
cat.sound()