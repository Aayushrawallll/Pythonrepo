from app import app, db  # Import app & db from app.py

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Will be hashed

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date, nullable=False)
    borrower = db.Column(db.String(255), nullable=True)  # Optional field

# Create tables in the database
if __name__ == '__main__':  
    with app.app_context():  # Ensure the app context is active
        db.create_all()
        print("Database tables created successfully!")
