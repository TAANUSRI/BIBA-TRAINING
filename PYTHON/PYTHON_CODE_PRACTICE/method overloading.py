class Animal:
    def make_sound(self):
        print("Animal makes a generic sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
class Bulldog(Dog):
    def make_sound(self):
        print("Bulldog growls")
animal_instance = Animal()
animal_instance.make_sound()  
dog_instance = Dog()
dog_instance.make_sound()  
bulldog_instance = Bulldog()
bulldog_instance.make_sound() 
