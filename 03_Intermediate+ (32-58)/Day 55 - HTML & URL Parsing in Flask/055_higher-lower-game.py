from flask import Flask
from random import randint

# Create a Flask app instance
app = Flask(__name__)

# Generate a random number between 0 and 9 once when the server starts
random_number = randint(0, 9)
print(f"Random number is: {random_number}")  # Print the number for debugging (visible in the console)


# --- Helper Function --- #
def styled_response(message, gif_url):
    """
    Returns an HTML response with a message and an image (GIF).
    Makes it easy to reuse the same HTML structure across routes.
    """
    return f"<h1>{message}</h1><img src='{gif_url}'>"


# --- Routes --- #

@app.route("/")
def home():
    """
    Root route ("/").
    Displays a welcome message and prompts the user to guess a number.
    """
    return styled_response(
        "Guess a number between 0 and 9",
        "https://media3.giphy.com/media/qq7ef70oHLoAM/giphy.gif?cid=ecf05e4760j787uoe3in9hzegleooxi75giew1zjpe05bezo&rid=giphy.gif&ct=g"
    )


@app.route("/<int:guess>")
def check_guess(guess):
    """
    This route handles user guesses passed in the URL, e.g., /5.
    It compares the guess to the random number and returns:
    - "Too low!" if the guess is lower
    - "Too high!" if the guess is higher
    - "Right number!" if the guess is correct
    Each response includes a fun GIF.
    """
    if guess < random_number:
        return styled_response(
            "Too low!",
            "https://media2.giphy.com/media/fnix5judzLJDJTaLgm/giphy.gif?cid=790b7611e2881bbb1c09734447bb8740e05708df8b2414d5&rid=giphy.gif&ct=g"
        )
    elif guess > random_number:
        return styled_response(
            "Too high!",
            "https://media1.giphy.com/media/CvgezXSuQTMTC/giphy.gif?cid=790b761103fd94ab86e553a8016f273249ffb20b2e6988d0&rid=giphy.gif&ct=g"
        )
    else:
        return styled_response(
            "Right number!",
            "https://media2.giphy.com/media/j9iwmVGwK4U1y/giphy.gif?cid=790b761118d53b6c603f6cc99cddd83a3705a7dc31783ea3&rid=giphy.gif&ct=g"
        )


# --- App Runner --- #
if __name__ == "__main__":
    # Starts the Flask development server in debug mode
    app.run(debug=True)
