from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Securely Generate a JWT Secret Key
app.config['JWT_SECRET_KEY'] = os.urandom(24).hex()  # Change this to a strong secret key

# Configure MySQL Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:aayushrawal@localhost/book_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Hashed password

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date, default=datetime.utcnow)
    borrower = db.Column(db.String(255), nullable=True)

# Create Database Tables
with app.app_context():
    db.create_all()

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except:
        return jsonify({"error": "Username already exists"}), 400

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    user = User.query.filter_by(username=data['username']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials!"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"token": access_token})

# Get all books (Protected Route)
@app.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "date_added": book.date_added.strftime('%Y-%m-%d'),
            "borrower": book.borrower
        }
        for book in books
    ])

# Add a New Book (Protected)
@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.json
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Title and author are required"}), 400

    new_book = Book(
        title=data['title'],
        author=data['author'],
        borrower=data.get('borrower', None)
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book added successfully!"}), 201

# Update a Book (Protected)
@app.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    data = request.json
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'borrower' in data:
        book.borrower = data['borrower']

    db.session.commit()

    return jsonify({"message": "Book updated successfully!"})

# Delete a Book (Protected)
@app.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
