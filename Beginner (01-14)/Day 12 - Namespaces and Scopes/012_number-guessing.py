import random

lives = 0  # Number of attempts the player has.


# Function to set the difficulty level.
def set_difficulty():
    """
    Ask the player to choose a difficulty level.
    Returns:
        int: Number of lives based on the chosen difficulty.
    """
    game_mode = int(input("Game Mode: \n[1] Easy - 10 lives \n[2] Hard - 5 lives\nChoose the difficulty: "))
    if game_mode == 1:
        return 10  # Easy mode gives 10 lives.
    else:
        return 5  # Hard mode gives 5 lives.


# Function to check if the player's guess is correct.
def check_guess(guess, goal):
    """
    Compare the guess with the goal and provide feedback.

    Parameters:
        guess (int): The player's guessed number.
        goal (int): The randomly generated target number.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    if guess < goal:
        print("Too low. Try again.")
    elif guess > goal:
        print("Too high. Try again.")
    return guess == goal  # Return True if the guess is correct.


# Main game loop
while True:
    print("Welcome to the number guessing game!\n")
    goal = random.randint(1, 100)  # Generate a random number between 1 and 100.
    lives = set_difficulty()  # Get the number of lives based on difficulty.
    print()

    # Loop to process the player's guesses.
    while lives > 0:
        print(f"Lives left: {lives}")
        guess = int(input("Guess the number (1 - 100): "))  # Ask the player for a guess.
        print()

        if check_guess(guess, goal):  # Check if the guess is correct.
            print("Congratulations! You won!")
            break  # Exit the loop if the player wins.

        lives -= 1  # Deduct a life if the guess is incorrect.
        if lives == 0:
            print("You have 0 lives! You lost!")  # Notify the player they lost.
            break

    # Ask the player if they want to play again.
    again = input("Do you want to play again? [Y] or [N]: ").upper()
    if again != "Y":
        print("Thanks for playing!")  # Exit message.
        break  # Exit the game loop.
