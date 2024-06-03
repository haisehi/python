from abc import ABC,abstractmethod
import math

class Shape():
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    #constructor
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def square(self):
        return self.__width * self.__height

    def perimeter(self):
        return  (self.__width + self.__height)*2

    def __str__(self):
        return f"Rectangle(width={self.__width}, height={self.__height}, square={self.square()}, perimeter={self.perimeter()})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, square={self.square()}, perimeter={self.perimeter()})"

# Example usage
rectangle = Rectangle(3, 4)
print(rectangle)

circle = Circle(5)
print(circle)