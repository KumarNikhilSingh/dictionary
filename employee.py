class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def employee_detail(self):
        print(f"Employee: {self.name} Position: {self.position} Salary: {self.salary} ")
employee = Employee("Mohan", "clerk", 45000)
employee.employee_detail()