# Grandfather class
class Grandfather:
    def __init__(self, name):
        self.name = name
    def display_grandfather(self):
        return f"Grandfather: {self.name}"
# Father class inheriting from Grandfather
class Father(Grandfather):
    def __init__(self, name, occupation):
        Grandfather.__init__(self, name)
        self.occupation = occupation
    def display_father(self):
        return f"{Grandfather.display_grandfather(self)}\nFather: {self.name}, Occupation: {self.occupation}"
# Son class inheriting from both Grandfather and Father
class Son( Father):
    def __init__(self, name, occupation, hobby):
        Grandfather.__init__(self, name)
        Father.__init__(self, name, occupation)
        self.hobby = hobby
    def display_son(self):
        return "{}\nFather: {}, Occupation: {}\nSon: {}, Hobby: {}".format(
            Grandfather.display_grandfather(self),
            self.name,
            self.occupation,
            self.name,
            self.hobby
        )
son_instance = Son("John III", "Student", "Playing video games")
print(son_instance.display_son())
