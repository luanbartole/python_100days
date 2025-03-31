import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
choice = ""  # Variable to control the while loop.


def caesar_cipher(operation, plain_text, shift_amount):
    """
    Function to encode or decode a message using the Caesar cipher.

    Parameters:
    operation (str): 'encode' to encrypt, 'decode' to decrypt.
    plain_text (str): The message to be processed.
    shift_amount (int): The number of positions to shift in the alphabet.
    """
    cipher_text = ""  # Variable to store the resulting text.

    for letter in plain_text:  # Iterate through each letter in the input text.
        try:
            index = alphabet.index(letter)  # Find the index of the letter in the alphabet.

            if operation == "encode":
                index += shift_amount  # Shift forward for encryption.
            elif operation == "decode":
                index -= shift_amount  # Shift backward for decryption.

            # Ensure the index wraps around the alphabet length if it goes beyond bounds.
            index = index % len(alphabet)

            cipher_text += alphabet[index]  # Append the new letter to the result.
        except ValueError:
            # If the letter is not in the alphabet (e.g., space, punctuation), keep it unchanged.
            cipher_text += letter

    print(f"Here is the {operation}d result: {cipher_text}")  # Print the result.


while choice != "no":  # Loop until the user decides to stop.
    print(art.logo)  # Display the logo from the imported 'art' module.

    # Ask the user for input parameters.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(direction, text, shift)

    choice = input("Do you want to continue? [Yes] or [No]\n").lower()
    print()
