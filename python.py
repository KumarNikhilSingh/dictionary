class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("Hindi")

child = Child()
print(child.speaks)    
    