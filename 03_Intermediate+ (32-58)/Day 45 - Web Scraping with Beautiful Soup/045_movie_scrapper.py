from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import requests  # Import requests to make HTTP requests

# URL of the archived webpage listing the best movies
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL and store the response
response = requests.get(URL)

# Extract the HTML content from the response
website_html = response.text

# Parse the HTML content with BeautifulSoup using the built-in HTML parser
soup = BeautifulSoup(website_html, "html.parser")

# Find all <h3> tags with the class "title" (each contains a movie title)
all_movies = soup.find_all(name="h3", class_="title")

# Extract the text from each <h3> tag to get the movie titles
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the list of movie titles (to have them in desired order)
movies = movie_titles[::-1]

# Open (or create) a file named "movies.txt" in write mode with UTF-8 encoding
with open("movies.txt", mode="w", encoding="utf-8") as file:
    # Write each movie title to the file, one per line
    for movie in movies:
        file.write(f"{movie}\n")
