import random
import hangman_art
import hangman_words

# Select a random word from the word list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

# Game status variables
end_of_game = False  # Tracks if the game has ended
lives = 6  # Total number of attempts allowed

print(hangman_art.logo)  # Display the hangman game logo

# Debugging hint (remove this in production)
print(f'Pssst, the solution is {chosen_word}.')

# Create a list to store the correct guesses (initially filled with underscores)
display = []
guesses = []  # List to track guessed letters
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # Prompt user for input and convert to lowercase

    # Check if the letter has already been guessed
    if guess in guesses:
        print("You have already guessed this letter. Try another one.")

    # Replace blanks with correctly guessed letters
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if the guessed letter is incorrect
    if guess not in chosen_word and guess not in guesses:
        print(f"The letter {guess} is not in the word. Try another one.")
        lives -= 1  # Reduce the number of attempts left

        if lives == 0:  # If no lives remain, end the game
            end_of_game = True
            print("You lose.")

    # Display the current progress of the word
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed correctly
    if "_" not in display:
        end_of_game = True
        print("You win.")

    guesses += guess  # Add guessed letter to the list of guesses
    print(hangman_art.stages[lives])  # Display the hangman stage based on remaining lives
