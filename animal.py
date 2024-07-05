class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        print(f"The {self.species} named {self.name} makes sound.")

animal = Animal("Cow", "Laado")
animal.make_sound()