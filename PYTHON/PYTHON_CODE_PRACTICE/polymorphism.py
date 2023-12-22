class Shape:
    def __init__(self, side_length):
        self.side_length = side_length
    def calculate_area(self):
        pass
class Square(Shape):
    def calculate_area(self):
        return self.side_length ** 2
class Circle(Shape):
    def calculate_area(self):
        import math
        return math.pi * self.side_length ** 2
def print_area(shape):
    print(f"Area: {shape.calculate_area()}")
square = Square(4)
circle = Circle(3)
print_area(square)  
print_area(circle)  
