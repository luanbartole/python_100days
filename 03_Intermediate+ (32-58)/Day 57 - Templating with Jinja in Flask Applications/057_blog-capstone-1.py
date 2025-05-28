# Import necessary modules from Flask and requests library
from flask import Flask, render_template
import requests

# Create an instance of the Flask class (our web app)
app = Flask(__name__)

# URL of the API endpoint containing blog post data
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

# Send a GET request to the blog API and convert the response to JSON format
response = requests.get(blog_url)
all_posts = response.json()

# Calculate the total number of blog posts
number_of_posts = len(all_posts)

# Define the route for the homepage
@app.route('/')
def home():
    # Render the index.html template and pass blog posts and their total count to it
    return render_template("index.html", posts=all_posts, total_posts=number_of_posts)

# Define a dynamic route to view individual blog posts based on their index
@app.route('/post/<post_index>')
def get_post(post_index):
    # Convert the post index from the URL (string) to an integer and adjust for zero-based indexing
    id = int(post_index) - 1
    # Render the post.html template and pass the selected blog post to it
    return render_template("post.html", post=all_posts[id])

# Start the Flask development server if this file is run directly
if __name__ == "__main__":
    # Run the app in debug mode (helpful for development and debugging)
    app.run(debug=True)
