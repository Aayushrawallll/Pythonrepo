import math

# Base class
class Shape:
    def area(self):
        pass  

    def perimeter(self):
        pass  

# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  

    def perimeter(self):
        return 4 * self.side  

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2 * (self.length + self.width) 

# Triangle class
class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a  
        self.b = b  
        self.c = c  
        self.height = height  

    def area(self):
        return 0.5 * self.b * self.height  

    def perimeter(self):
        return self.a + self.b + self.c  
# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius  

    def perimeter(self):
        return 2 * math.pi * self.radius  

# Creating objects for each shape
square = Square(4)
rectangle = Rectangle(5, 3)
triangle = Triangle(3, 4, 5, 4)
circle = Circle(5)

# Results
print("Square -> Area:", square.area(), "| Perimeter:", square.perimeter())
print("Rectangle -> Area:", rectangle.area(), "| Perimeter:", rectangle.perimeter())
print("Triangle -> Area:", triangle.area(), "| Perimeter:", triangle.perimeter())
print("Circle -> Area:", round(circle.area(), 2), "| Perimeter:", round(circle.perimeter(), 2))
