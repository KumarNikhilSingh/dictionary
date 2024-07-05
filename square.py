class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        print(f"Area of Square is : {self.length * self.length}")

    def paremeter(self):
        print(f"Paremeter of Square is : {self.length * 4}")

length = Square(12)
length.area()
length.paremeter()