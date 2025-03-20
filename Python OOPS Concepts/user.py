class User:
    def __init__(self, fname, lname, add1, add2, email, mob_no):
        self.fname = fname
        self.lname = lname
        self.add1 = add1
        self.add2 = add2
        self.email = email
        self.mob_no = mob_no

    def display_info(self):
        print(f"\nName: {self.fname} {self.lname}")
        print(f"\nAddress: {self.add1}, {self.add2}")
        print(f"\nEmail: {self.email}")
        print(f"\nMobile No: {self.mob_no}")

# Manual Data Entry
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
add1 = input("Enter Address Line 1: ")
add2 = input("Enter Address Line 2: ")
email = input("Enter Email: ")
mob_no = input("Enter Mobile Number: ")

user1 = User(fname, lname, add1, add2, email, mob_no)
user1.display_info()
