class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def display_output(self):
        print(f" Name: {self.name}")
        print(f" Country: {self.country}")
        print(f" Date Of Birth {self.date_of_birth}")

person1 = Person("Nikhil", "India", "2000-4-18")
person2 = Person("De Mellow", "USA", "1995-11-2")
person3 = Person("Jordan", "SA", "1996-12-30")

person1.display_output() 
print("                ")      
person2.display_output()
print("                ")
person3.display_output()