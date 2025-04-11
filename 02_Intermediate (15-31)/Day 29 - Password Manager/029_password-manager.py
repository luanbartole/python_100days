# Import necessary modules
from tkinter import *                # GUI toolkit
from tkinter import messagebox       # Popup message boxes
from random import randint, choice, shuffle  # Used for random password generation
import pyperclip                     # Lets us copy text to the clipboard

# Default email that auto-fills in the UI
EMAIL = "email@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Character pools for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly pick 8-10 letters, 2-4 symbols, and 2-4 numbers
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)  # Shuffle the characters to make the password more secure

    password = "".join(password_list)  # Join list into a single string

    # Insert generated password into the entry field and copy it to clipboard
    pass_entry.delete(0, "end")
    pass_entry.insert(0, password)
    pyperclip.copy(password)  # Automatically copies password for convenience


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get input data from the user
    web_text = website_entry.get()
    login_text = login_entry.get()
    pass_text = pass_entry.get()
    final_text = f"{web_text} | {login_text} | {pass_text}\n"

    # Check if any fields are empty
    if len(web_text) == 0 or len(login_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        # Ask user to confirm before saving
        is_ok = messagebox.askokcancel(
            title=web_text,
            message=f"Details entered were as follows: \nEmail: {login_text} \nPassword:{pass_text} \nSave data?"
        )
        if is_ok:
            # Save the data into a text file
            with open("data.txt", "a") as data_file:
                data_file.write(final_text)
            # Clear fields after saving
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by Luan Bartole")
window.config(padx=50, pady=50)  # Add padding to the window

# Add logo image using Canvas
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=0, row=0, columnspan=3)

# Website label + entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=59)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()  # Focus cursor on this field at start

# Email/Username label + entry
login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_entry = Entry(width=59)
login_entry.grid(column=1, row=2, columnspan=2, sticky="w")
login_entry.insert(0, EMAIL)  # Auto-fill default email

# Password label + entry + generate button
pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=40)
pass_entry.grid(column=1, row=3, sticky="w")

genpass_button = Button(text="Generate Password", command=generate_password)
genpass_button.grid(column=2, row=3, sticky="w")

# Add/save button
addpass_button = Button(text="Add", width=50, command=save)
addpass_button.grid(column=1, row=4, columnspan=2, sticky="w")

# Start the GUI event loop
window.mainloop()
