from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aayushrawal@localhost/booksdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price
        }

# Create Tables
with app.app_context():
    db.create_all()

# GET All Books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])
'''
 POST Add Book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], price=data['price'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!"}), 201
'''
#POST for multiple dataset
@app.route('/books', methods=['POST'])
def add_books():
    data = request.json  # Expecting a list of books
    
    # Ensure data is a list
    if not isinstance(data, list):
        return jsonify({"error": "Expected a list of books"}), 400

    added_books = []
    for item in data:
        if 'title' not in item or 'author' not in item or 'price' not in item:
            return jsonify({"error": "Each book must have title, author, and price"}), 400
        
        try:
            new_book = Book(
                title=item['title'],
                author=item['author'],
                price=float(item['price'])  # Convert price to float
            )
            db.session.add(new_book)
            added_books.append(item)  # Save successfully added books
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    db.session.commit()
    return jsonify({"message": "Books added successfully!", "books": added_books}), 201




# PUT Update Book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found!"}), 404
    
    data = request.json
    book.title = data['title']
    book.author = data['author']
    book.price = data['price']

    db.session.commit()
    return jsonify({"message": "Book updated successfully!"})

# DELETE Book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found!"}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
