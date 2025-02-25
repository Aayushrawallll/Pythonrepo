import psycopg2

# connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname="user_management",
        user="postgres",
        password="aayushrawal",
        host="localhost",
        port="5432"
    )

# add a user
def add_user(name, email):
    conn = connect_db()
    cur = conn.cursor()
    
    try:
        cur.execute("INSERT INTO user_mgmt (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        print(f"User {name} added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    
    cur.close()
    conn.close()

# get a user by ID
def get_user(user_id):
    conn = connect_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM user_mgmt WHERE id = %s", (user_id,))
        user = cur.fetchone()
        
        if user:
            print(f"User Found: ID={user[0]}, Name={user[1]}, Email={user[2]}")
        else:
            print(" User Not Found.")
    except Exception as e:
        print(f" Error: {e}")
    
    cur.close()
    conn.close()

#get all users
def get_all_users():
    conn = connect_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM user_mgmt")
        users = cur.fetchall()
        
        if users:
            print("All Users:")
            for user in users:
                print(f"🔹 ID={user[0]}, Name={user[1]}, Email={user[2]}")
        else:
            print("No users found.")
    
    except Exception as e:
        print(f" Error: {e}")
    
    cur.close()
    conn.close()

# delete a user by ID
def delete_user(user_id):
    conn = connect_db()
    cur = conn.cursor()
    
    try:
        cur.execute("DELETE FROM user_mgmt WHERE id = %s", (user_id,))
        conn.commit()
        print(f"🗑️ User {user_id} deleted successfully!")
    except Exception as e:
        print(f" Error: {e}")
    
    cur.close()
    conn.close()

# Menu-driven approach
def main():
    while True:
        print("\nUser Management System")
        print("1 Add User")
        print("2 Get User by ID")
        print("3 Get All Users")
        print("4 Delete User by ID")
        print("5 Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            add_user(name, email)

        elif choice == "2":
            try:
                user_id = int(input("Enter User ID: "))
                get_user(user_id)
            except ValueError:
                print("Invalid input!.")

        elif choice == "3":
            get_all_users()

        elif choice == "4":
            try:
                user_id = int(input("Enter User ID to Delete: "))
                delete_user(user_id)
            except ValueError:
                print("Invalid input! ")

        elif choice == "5":
            print("Exit...")
            break

        else:
            print("Invalid choice! ")

# Run the program
if __name__ == "__main__":
    main()
