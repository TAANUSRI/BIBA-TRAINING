# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
# Child class (Derived class)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks loudly")
my_dog = Dog("pomarian")
my_dog.speak()  
my_dog.bark()   



