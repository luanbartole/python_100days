# Import necessary modules from Flask and extensions
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'  # Used for session management and flash messages

# Define SQLAlchemy Base for ORM mapping
class Base(DeclarativeBase):
    pass

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect here if user is not logged in

# Define User model using SQLAlchemy ORM and Flask-Login's UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))  # Hashed password
    name: Mapped[str] = mapped_column(String(1000))

# Create the database tables
with app.app_context():
    db.create_all()

# Load a user by ID for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Home route
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# Register route: Handles new user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if user already exists
        if db.session.execute(db.select(User).filter_by(email=request.form.get('email'))).scalar():
            flash("User already exists, please log in.")
            return redirect(url_for('login'))

        # Hash and salt the password securely
        hash_and_salted_password = generate_password_hash(
            password=request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        # Create a new user object and store it in the database
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()

        # Log the user in and redirect to secrets page
        login_user(new_user)
        return render_template("secrets.html")

    return render_template("register.html", logged_in=current_user.is_authenticated)

# Login route: Authenticates user credentials
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar()

        # Validate user credentials
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password. Please try again.")
            return redirect(url_for('login'))

    return render_template("login.html")

# Secrets route: Protected page that requires login
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)

# Logout route: Logs the user out and redirects to home
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Download route: Allows logged-in users to download a file
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
