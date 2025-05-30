from flask import Flask, render_template
import requests
from selenium.webdriver.support.expected_conditions import none_of

posts = requests.get("https://api.npoint.io/cbaab53bf075ab46cda7").json()
app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")