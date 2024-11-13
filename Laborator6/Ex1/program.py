import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(a=3, b=4, c=5)

print("Circle:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("\nRectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

print("\nTriangle:")
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())