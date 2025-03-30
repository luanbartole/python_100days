import art  # Import art module for displaying logo or other artworks
import random  # Import random module for generating random numbers


def line(number):
    """
    Function to print a separator line of a given length.

    Parameters:
    number (int): The number of '=' characters to print.
    """
    print("=" * number)


def deal_card(deal_number):
    """
    Function to deal a specified number of random cards.

    Parameters:
    deal_number (int): The number of cards to be dealt.

    Returns:
    list: A list of random cards, where each card is represented by an integer.
    """
    new_hand = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Deck of cards, 11 represents Ace
    for x in range(0, deal_number):  # Loop to deal the required number of cards
        new_hand.append(random.choice(cards))  # Add a random card to the hand
    return new_hand


def calculate_score(card_list):
    """
    Function to calculate the total score of a hand of cards.

    Parameters:
    card_list (list): A list of integers representing the player's or dealer's cards.

    Returns:
    int: The total score of the hand. A score of 0 represents a blackjack.
    """
    if len(card_list) == 2 and sum(card_list) == 21:  # Special case: blackjack
        return 0  # Blackjack is represented by a score of 0
    else:
        if sum(card_list) > 21 and 11 in card_list:  # If score exceeds 21, replace Ace (11) with 1
            card_list.remove(11)
            card_list.append(1)
        return sum(card_list)


def compare(player, dealer):
    """
    Function to compare the scores of the player and the dealer.

    Parameters:
    player (int): The player's score.
    dealer (int): The dealer's score.

    Returns:
    str: "Player" if the player wins, "Computer" if the dealer wins, or "Draw" if it's a tie.
    """
    if player == dealer:  # If scores are equal, it's a draw
        return "Draw"
    elif player > 21 and dealer > 21:  # Both players bust, it's a draw
        return "Draw"
    elif player == 0 or dealer > 21:  # Player has blackjack or dealer busts, player wins
        return "Player"
    elif dealer == 0 or player > 21:  # Dealer has blackjack or player busts, dealer wins
        return "Computer"
    elif player > dealer:  # If player score is greater, player wins
        return "Player"
    else:  # If dealer score is greater, dealer wins
        return "Computer"


# Main game loop
endgame = False  # A flag to control the game loop

while not endgame:  # Loop to keep the game running until the player decides to stop
    print(art.logo)  # Display the game logo (imported from art.py)

    # Deal 2 cards to both the player and the dealer
    user_cards = deal_card(2)
    computer_cards = deal_card(2)

    # Calculate scores for both player and dealer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Show the player's and dealer's cards and scores
    print(f"Your Cards: {user_cards}")
    print(f"Your Score: {user_score}")
    print(f"Computer's First Card: {computer_cards[0]}\n")

    # Check if the player has a blackjack
    if user_score == 0:
        print("You have a blackjack! You win!")
        endgame = True  # End the game

    # Check if the dealer has a blackjack
    elif computer_score == 0:
        print("The computer has a blackjack! You lose!")
        endgame = True  # End the game

    else:  # If neither has blackjack, allow the player to decide to draw more cards
        while not endgame and input("Do you wanna draw another card? [Y] or [N] ").upper() != "N":
            new_card = deal_card(1)  # Deal one new card to the player
            user_cards.append(new_card[0])  # Add the new card to the player's hand
            user_score = calculate_score(user_cards)  # Recalculate the player's score

            line(75)
            print(f"Your Cards: {user_cards}")  # Show the player's cards
            print(f"Your Score: {user_score}")  # Show the player's score
            print(f"Computer's First Card: {computer_cards[0]}")  # Show the computer's first card
            line(75)

            # Check if the player has busted (score > 21)
            if user_score > 21:
                print("You went over 21!")
                endgame = True  # End the game

            # Check if the player has a blackjack after drawing a card
            if user_score == 0:
                print("You have a blackjack!")
                endgame = True  # End the game

        # Dealer's turn to draw cards if the player hasn't busted
        while computer_score < 17:
            new_card = deal_card(1)  # Deal one new card to the dealer
            computer_cards.append(new_card[0])  # Add the new card to the dealer's hand
            computer_score = calculate_score(computer_cards)  # Recalculate the dealer's score

            # Check if the dealer has busted
            if user_score > 21:
                print("The computer went over 21!")
                endgame = True  # End the game

            # Check if the dealer has a blackjack
            if computer_score == 0:
                print("The computer has a blackjack!")
                endgame = True  # End the game

        # Display the final hands and scores of both the player and the dealer
        line(75)
        print(f"Your Cards: {user_cards}")
        print(f"Your Score: {user_score}")
        print(f"Computer Cards: {computer_cards}")
        print(f"Computer Score: {computer_score}")
        line(75)

        # Determine the winner using the compare function
        winner = compare(user_score, computer_score)
        if winner == "Draw":
            print("It was a Draw")
        else:
            print(f"Winner: {winner}")  # Announce the winner

        line(75)

    # Ask if the player wants to play another game
    if input("Do you wanna play another game? [Y/N] ").upper() == "N":
        endgame = True  # End the game if the player chooses 'N'
    else:
        endgame = False  # Restart the game if the player chooses 'Y'

    line(75)
