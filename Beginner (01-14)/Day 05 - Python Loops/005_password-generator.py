# Password Generator Project
import random  # Importing the random module to select random characters

# Lists containing possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# User input for number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""  # Initializing an empty string to store the password

# Adding random letters to the password
for letter in range(nr_letters):
    password += random.choice(letters)

# Adding random symbols to the password
for symbol in range(nr_symbols):
    password += random.choice(symbols)

# Adding random numbers to the password
for number in range(nr_numbers):
    password += random.choice(numbers)

# Shuffling the password to randomize the character order
password = ''.join(random.sample(password, len(password)))

# Display the generated password
print(f"Your generated password is: {password}")
