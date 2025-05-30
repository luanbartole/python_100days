from flask import Flask, render_template
import requests

# Fetch the blog posts from an external JSON API and parse it as Python data
posts = requests.get("https://api.npoint.io/cbaab53bf075ab46cda7").json()

# Create a new Flask web application
app = Flask(__name__)

# Define the route for the homepage, which shows all blog posts
@app.route("/")
def get_all_posts():
    # Renders index.html and passes all posts to the template
    return render_template("index.html", all_posts=posts)

# Define the route for the contact page (static)
@app.route("/contact.html")
def contact():
    # Simply renders the contact page template
    return render_template("contact.html")

# Define the route for the about page (static)
@app.route("/about.html")
def about():
    # Simply renders the about page template
    return render_template("about.html")

# Define a dynamic route for showing a specific blog post by its ID
@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    # Loop through all posts to find the one with the matching ID
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    # Renders the post.html template with the selected blog post
    return render_template("post.html", post=requested_post)

# Run the Flask development server locally
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")