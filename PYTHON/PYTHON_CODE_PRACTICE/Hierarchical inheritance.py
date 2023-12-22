# Base class
class Animal:
    def __init__(self, name):
        self.name = name
def eat(self):
        print(f"{self.name} is eating")
# Derived class 1
class Mammal(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping")
# Derived class 2
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")
mammal_instance = Mammal("Dog")
mammal_instance.eat()   
mammal_instance.sleep() 
bird_instance = Bird("Eagle")
bird_instance.eat()    
bird_instance.fly()   
