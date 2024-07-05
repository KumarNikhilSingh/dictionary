class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


    def display_student(self):
        print(f"Student Name: {self.name} Student_ ID {self.student_id} ")

student = Student("Rajat", 201)
student.display_student()