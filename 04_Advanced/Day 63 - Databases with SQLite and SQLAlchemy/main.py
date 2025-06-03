from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy extension
db = SQLAlchemy(app)

# ---------------------------- DB MODEL ----------------------------- #
# Define Book model for the database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each book
    title = db.Column(db.String(250), unique=True, nullable=False)  # Book title
    author = db.Column(db.String(250), nullable=False)  # Author name
    rating = db.Column(db.Float, nullable=False)  # Book rating

    def __repr__(self):
        return f"<Book {self.title}>"

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# ---------------------------- ROUTES ------------------------------- #

# Home route – displays all books in the database
@app.route('/')
def home():
    all_books = Book.query.all()  # Retrieve all books
    return render_template("index.html", all_books=all_books)

# Add book route – handles both form display and submission
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # Create a new Book object from form data
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = float(request.form["rating"])
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

# Edit rating route – allows user to update the book's rating
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)  # Fetch book or return 404 if not found
    if request.method == "POST":
        book.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

# Delete book route – removes a book from the database
@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Book, book_id)  # Fetch book or return 404
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")