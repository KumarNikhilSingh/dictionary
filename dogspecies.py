class Dog:
    species = "canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old")

    def speak(self, sound):
        print(f"{self.name} says {sound}")

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 6)

miles.description()
miles.speak("Woof")

buddy.description()
buddy.speak("bark")