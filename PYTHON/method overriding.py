class Animal:
    def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
animal_instance = Animal()
animal_instance.make_sound() 
dog_instance = Dog()
dog_instance.make_sound() 
cat_instance = Cat()
cat_instance.make_sound()  
