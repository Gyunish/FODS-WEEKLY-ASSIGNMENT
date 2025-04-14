#making a class for student information
class Student:
    def __init__(self, student_id="", name="", address="", admission_year=0, level="", section=""):
        self.student_id=student_id
        self.name=name
        self.address=address
        self.admission_year=admission_year
        self.level=level
        self.section=section

    #function to ask input
    def input_details(self):
        print("\nEnter Student Details:")
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Full Name: ")
        self.address = input("Enter Address: ")
        self.admission_year = int(input("Enter Admission Year: "))
        self.level = input("Enter Level: ")
        self.section = input("Enter Section: ")

    #function to display details
    def display_details(self):
        print("\nStudent Information:")
        print("Student ID:",self.student_id)
        print("Name:",self.name)
        print("Address:",self.address)
        print("Admission Year:",self.admission_year)
        print("Level:",self.level)
        print("Section:",self.section)

student=Student()
student.input_details()
student.display_details()