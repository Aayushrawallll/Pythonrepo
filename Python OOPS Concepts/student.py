class Student:
    def __init__(self, fname, lname, roll_no, age, gender, class_name, marks):
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.marks = marks

    def display_info(self):
        print(f"\nName: {self.fname} {self.lname}")
        print(f"\nRoll No: {self.roll_no}")
        print(f"\nAge: {self.age}")
        print(f"\nGender: {self.gender}")
        print(f"\nClass: {self.class_name}")
        print(f"\nMarks: {self.marks}")

# Manual Data Entry
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
roll_no = input("Enter Roll Number: ")
age = input("Enter Age: ")
gender = input("Enter Gender: ")
class_name = input("Enter Class: ")
marks = input("Enter Marks: ")

student1 = Student(fname, lname, roll_no, age, gender, class_name, marks)
student1.display_info()
