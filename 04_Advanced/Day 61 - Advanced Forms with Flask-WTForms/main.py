from flask import Flask, render_template, redirect, url_for
from forms import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "your_secret_key" # Required for CSRF protection
bootstrap = Bootstrap5(app)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="5000")