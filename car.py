class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    
    def running_on_road(self):
        print(f"The {self.name} {self.model} {self.year} car running of the road")

car = Car("Toyota", "Corolla", 2020)
car.running_on_road()