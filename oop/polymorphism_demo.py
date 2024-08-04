import math

class Shape:
    def area(self):
        """Method that should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the attributes for a rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the attributes for a circle."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
