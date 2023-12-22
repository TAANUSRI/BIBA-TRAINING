# Parent class (Base class)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
# Child class (Derived class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
# Another child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")
print(my_dog.speak())  
print(my_cat.speak())  
