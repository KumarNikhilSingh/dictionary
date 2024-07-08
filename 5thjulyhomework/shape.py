import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of circle is: {math.pi * self.radius ** 2}")

    def perimeter(self):
        print(f"Perimeter of Circle is: {2 * math.pi * self.radius}")

class Square(Shape):
        def __init__(self, side_length):
            self.side_length = side_length

        def area(self):
            print(f"Area of square: {self.side_length ** 2}")

        def perimeter(self):
            print(f"peremeter of square: {self.side_length * 4 }")

class Triangle(Shape):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def area(self):
            print(f" Area of triangle is: {(self.a + self.b + self.c) / 2} ")

        def perimeter(self):
            print(f" Perimeter of triangle is: {self.a + self.b + self.c}")
        


circle = Circle(5)
circle.area()
circle.perimeter()

print("\n")

square = Square(4)
square.area()
square.perimeter()

print("\n")

triangle = Triangle(3, 4, 5) 
triangle.area()
triangle.perimeter()



       

