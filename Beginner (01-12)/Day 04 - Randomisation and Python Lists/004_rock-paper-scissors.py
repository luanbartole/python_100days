import random

# Variables
rock = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""
scissors = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
hands = [rock,paper,scissors]

# Displaying the game options to the player
print("="*45)
print("[0] Rock / [1] Paper / [2] Scissors")
print("="*45)

# Player selects a hand by inputting a number, and the computer randomly selects one
player_hand = hands[int(input("Choose one: "))] # Converts player input to corresponding hand
computer_hand = random.choice(hands) # Randomly selects a hand for the computer

# Displaying the choices of both player and computer
print("="*25)
print(f"Player's Hand: \n{player_hand}\n")
print(f"Computer's Hand: \n{computer_hand}\n")

# Determining the winner
if player_hand == computer_hand:
    print("It's a draw") # Case where both players choose the same hand
else:
    # Checking win/loss conditions based on Rock-Paper-Scissors rules
    if player_hand == rock:
        if computer_hand == paper:
            print("You lost") # Paper beats rock
        else:
            print("You won") # Rock beats scissors
    if player_hand == paper:
        if computer_hand == scissors:
            print("You lost") # Scissors beats paper
        else:
            print("You won") # Paper beats rock
    if player_hand == scissors:
        if computer_hand == rock:
            print("You lost") # Rock beats scissors
        else:
            print("You won") # Scissors beats paper