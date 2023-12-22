# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
# Intermediate class inheriting from Animal
class Mammal(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping")
# Derived class inheriting from Mammal
class Dog(Mammal):
    def bark(self):
        print(f"{self.name} is barking")
my_dog = Dog("Golden Retriever")
my_dog.eat()    
my_dog.sleep()  
my_dog.bark()   
