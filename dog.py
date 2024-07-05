class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} {self.age}")

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)