class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area: {22 / 7 * (self.radius ** 2)}")

    def circumference(self):
        print(f"Circumference: {2 * (22 / 7 * self.radius)} ")   

circle =Circle(5)
circle.area()
circle.circumference()
     
    







'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of Rectangle is : {self.length * self.width}")

    def paremeter(self):
        print(f"Paremeter of Rectangle is : {2 * (self.length + self.width)}")


rectangle = Rectangle(12, 6)
rectangle.area()
rectangle.paremeter()   
'''