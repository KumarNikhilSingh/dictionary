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