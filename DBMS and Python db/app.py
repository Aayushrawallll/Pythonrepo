import mysql.connector

#connect to mysql
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="aayushrawal",
    database="user_mgmt"
)

cursor=db.cursor()

#add users
def add_users(name, email):
    sql = "INSERT INTO users(name,email) VALUES (%s,%s)"
    cursor.execute(sql, (name, email))
    db.commit()
    print("User added successfully!")

#get user by id
def get_user(user_id):
    sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql, (user_id),)
    user =  cursor.fetchone()
    if user:
        print("User Found: {user}")
    else:
        print("User not found!")

#to get all users
def get_all_users():
    sql = "SELECT *FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    for user in users:
        print(user)

#delete users 
def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    db.commit()
    print("User deleted successfully!")


#menu for user input 
while True:
    print("\n1.Add User")
    print("2. Get User by ID")
    print("3. Get All Users")
    print("4. Delete User")
    print("5. Exit")

    choice=input("Enter Choice: ")

    if choice == "1":
        name=input("Enter Name: ")
        email=input("Enter Email: ")
        add_users(name, email)
    elif choice=="2":
        user_id=int(input("Enter User ID: "))
        get_user(user_id) 
    elif choice=="3":
        get_all_users()
    elif choice=="4":
        user_id=int(input("Enter user Id to delete: "))
        delete_user(user_id)
    elif choice=="5":
        print("Exiting....")
        break
    else:
        print("Invalid choice! Try Again..")

cursor.close()
db.close()                       