class Person:
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Ram = Person("ram", 25)
sita = Person("sita", 30)
print("{} belongs to the species {}".format(Ram.name, Ram.__class__.species))
print("{} belongs to the species {}".format(sita.name, sita.__class__.species))
print("{} is {} years old".format(Ram.name, Ram.age))
print("{} is {} years old".format(sita.name, sita.age))
