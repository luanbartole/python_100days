# --- Standard Flask & Extensions Imports --- #
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

# --- The Movie Database (TMDb) API credentials --- #
TMD_TOKEN = os.environ.get("THE_MOVIE_DB_TOKEN")
TMD_API_KEY = os.environ.get("THE_MOVIE_DB_API_KEY")
TMD_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

# --- Flask App Setup --- #
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Required for CSRF protection in Flask-WTF forms

# --- SQLite Database Configuration --- #
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Initialize SQLAlchemy and Bootstrap --- #
db = SQLAlchemy(app)
Bootstrap5(app)

# ---------------------------- DATABASE MODEL ----------------------------- #
class Movie(db.Model):
    """Represents a movie entry in the database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()


# ---------------------------- FORMS ----------------------------- #
class RateMovieForm(FlaskForm):
    """Form for rating and reviewing a movie."""
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    """Form for entering a movie title to add."""
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# ---------------------------- ROUTES ----------------------------- #

@app.route("/")
def home():
    """
    Home page: Shows all movies ranked by rating in ascending order (best = highest rank).
    Rankings are dynamically assigned based on rating.
    """
    # Get movies sorted by highest rating first
    movies = Movie.query.order_by(Movie.rating.desc()).all()

    # Assign rankings based on order
    for i, movie in enumerate(movies):
        movie.ranking = i + 1
    db.session.commit()

    # Reverse the list so best-ranked movie appears at the bottom
    movies.reverse()

    return render_template("index.html", all_movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Add page: Form to input movie title. Sends request to TMDb to search for matching titles.
    """
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMD_TOKEN}"
        }

        # Call TMDb API to search for movie by title
        response = requests.get(TMD_SEARCH_URL, headers=headers, params={"query": movie_title})
        response.raise_for_status()
        data = response.json()["results"]

        # Keep only essential movie info to avoid large session data
        options = [
            {
                "id": movie["id"],
                "title": movie["title"],
                "release_date": movie.get("release_date", "N/A")
            } for movie in data
        ]
        session["options"] = options  # Store search results in session

        return redirect(url_for("select"))
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    """
    Select page: Displays TMDb search results as a list of options to choose from.
    """
    options = session.get("options", [])
    return render_template("select.html", options=options)


@app.route("/add_movie/<int:movie_id>")
def add_movie_to_db(movie_id):
    """
    When user selects a movie from TMDb search results, fetch full movie data and add to local DB.
    Redirect to edit page to rate and review it.
    """
    movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMD_TOKEN}"
    }

    response = requests.get(movie_details_url, headers=headers)
    response.raise_for_status()
    movie_data = response.json()

    # Extract required fields
    title = movie_data.get("title", "No title")
    img_url = f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path')}" if movie_data.get('poster_path') else ""
    year = int(movie_data.get("release_date", "0000-00-00")[:4]) if movie_data.get("release_date") else 0
    description = movie_data.get("overview", "No description available")

    # Add placeholder rating/review for now
    new_movie = Movie(
        title=title,
        img_url=img_url,
        year=year,
        description=description,
        rating=0.0,
        ranking=0,
        review=""
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', movie_id=new_movie.id))


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    """
    Edit page: Form to update the rating and review of a movie.
    """
    form = RateMovieForm()
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    """
    Delete a movie from the database.
    """
    movie_to_delete = db.get_or_404(Movie, movie_id)
    if movie_to_delete:
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for('home'))


# ---------------------------- RUN APP ----------------------------- #
if __name__ == '__main__':
    app.run(debug=True)
