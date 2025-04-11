from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

EMAIL = "email@gmail.com"

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web_text = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"Data file not found. \nTry adding a new account before searching one.")
    else:
        if web_text in json_data:
            login_text = json_data[web_text]["email"]
            pass_text = json_data[web_text]["password"]
            messagebox.showinfo(title=web_text, message=f"Email: {login_text} \nPassword: {pass_text}")
        else:
            messagebox.showinfo(title="Empty", message=f"{web_text} is not stored in the data file. \nTry another one.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
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
    new_data = {
        web_text: {
            "email": login_text,
            "password": pass_text,
        }
    }

    if len(web_text) == 0 or len(login_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", pady=10)
website_entry.focus()  # Focus cursor on this field at start

# Search Password
website_button = Button(text="Search", command=find_password, width=15, bd=0.5)
website_button.grid(column=2, row=1, sticky="e")

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