# Import required modules
import pandas
from tkinter import *
from tkinter import messagebox
from random import choice

# ---------------------------- CONSTANTS & GLOBAL VARIABLES ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"  # Light green background color for UI
FONT = "Ariel"                # Font used throughout the UI

# Try to load user's progress (words they still need to learn)
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If progress file doesn't exist, fall back to the original list
    data = pandas.read_csv("data/korean_words.csv")
finally:
    # Convert DataFrame to list of dictionaries, each with Korean and English word
    data_dict = data.to_dict(orient="records")

current_card = {}  # Will store the current word being shown


# ---------------------------- CREATE FLASH CARDS ------------------------------- #

def next_card():
    """Pick the next random Korean word to display and set a timer to flip it."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer

    # Choose a random word from the list
    current_card = choice(data_dict)

    # Update canvas with front side of the card
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_text, text="Korean", fill="black")
    canvas.itemconfig(word_text, text=current_card["Korean"], fill="black")

    # Set timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the card to reveal the English translation."""
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #

def save_progress():
    """Remove the current word from the list and save progress."""
    global data_dict

    # Remove the current word from the learning list
    data_dict.remove(current_card)

    # If all words have been learned, reset the list
    if not data_dict:
        new_data = pandas.read_csv("data/korean_words.csv")
        data_dict = new_data.to_dict(orient="records")
        messagebox.showinfo(
            title="Congratulations",
            message="You learned all the 100 words! \nI'm gonna reset the list now."
        )

    # Save updated learning list to CSV
    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)

    # Load the next word
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Main window
window = Tk()
window.title("Flash Card by Luan Bartole")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Start the timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Load images for cards and buttons
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_logo = PhotoImage(file="images/right.png")
wrong_logo = PhotoImage(file="images/wrong.png")

# Create the flashcard canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)  # Card image (front/back)
language_text = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))  # Language label
word_text = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))  # Word label
canvas.grid(column=0, row=0, columnspan=2)

# Right button (user knew the word)
right_button = Button(image=right_logo, highlightthickness=0, bd=0.1, command=save_progress)
right_button.grid(column=0, row=1)

# Wrong button (user didn't know the word)
wrong_button = Button(image=wrong_logo, highlightthickness=0, bd=0.1, command=next_card)
wrong_button.grid(column=1, row=1)

# Start by showing the first card
next_card()

# Keep the app running
window.mainloop()
