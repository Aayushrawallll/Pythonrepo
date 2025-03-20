class Person:
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def display_info(self):
        print(f"\nName: {self.fname} {self.lname}")
        print(f"\nGender: {self.gender}")

class Employee(Person):
    def __init__(self, fname, lname, gender, designation, department, salary, doj, dor):
        super().__init__(fname, lname, gender)
        self.designation = designation
        self.department = department
        self.salary = salary
        self.doj = doj
        self.dor = dor

    def display_info(self):
        super().display_info()
        print(f"\nDesignation: {self.designation}")
        print(f"\nDepartment: {self.department}")
        print(f"\nSalary: {self.salary}")
        print(f"\nDate of Joining: {self.doj}")
        print(f"\nDate of Retirement: {self.dor}")

# Manual Data Entry
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
gender = input("Enter Gender: ")
designation = input("Enter Designation: ")
department = input("Enter Department: ")
salary = input("Enter Salary: ")
doj = input("Enter Date of Joining (YYYY-MM-DD): ")
dor = input("Enter Date of Retirement (YYYY-MM-DD): ")

employee1 = Employee(fname, lname, gender, designation, department, salary, doj, dor)
employee1.display_info()
