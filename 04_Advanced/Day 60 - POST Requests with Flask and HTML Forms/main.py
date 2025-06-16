from flask import Flask, render_template, request
import requests
import smtplib
import os

# Load environment variables for email credentials
BOT_EMAIL = os.environ.get("PYTHON_EMAIL")
BOT_EMAIL_PASSWORD = os.environ.get("PYTHON_EMAIL_PASSWORD")
user_email = os.environ.get("USER_EMAIL")

# Get blog post data from an external JSON API
posts = requests.get("https://api.npoint.io/cbaab53bf075ab46cda7").json()

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage that displays all blog posts
@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)

# Route for the contact page, which handles both GET and POST requests
@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form  # Collect data submitted in the form

        # Send the form data via email using SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=BOT_EMAIL,
                to_addrs=user_email,
                msg=f"Subject: Blog Contact Form - {data['username']} \n\n"
                    f"Message: {data['message']} \n\n"
                    f"Email: {data['email']} Phone Number: {data['phone']}"
            )

        # Show a success message to the user
        return "<h1>Successfully sent your message</h1>"

    # Render the contact form template if it's a GET request
    return render_template("contact.html")

# Route for the about page
@app.route("/about.html")
def about():
    return render_template("about.html")

# Route for displaying an individual blog post based on its ID
@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    # Search for the post with the given ID
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5001")