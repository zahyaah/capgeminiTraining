class Animal: 
    def sound(self): 
        pass 
    def lifespan(self):
        pass 
    def about(self):
        pass 

class Elephant(Animal):
    def sound(self):
        print("Makes Elephant Sound!")
    def lifespan(self):
        print("Lives for around 50-60 years")
    def about(self):
        print("I'm huge, I'm strong and I've brains.")

class Tiger(Animal):
    def sound(self):
        print("Makes Tiger Sound!")
    def lifespan(self):
        print("Lives for around 15-20 years")
    def about(self):
        print("I'm fast, I'm strong and I've brains.")

E = Elephant() 
E.sound() 
E.lifespan() 
E.about() 

print()

T = Tiger()
T.sound()
T.lifespan() 
T.about()