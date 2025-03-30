import art

print(art.logo)  # Display the auction logo.
auction = {}  # Dictionary to store bidders' names as keys and their bids as values.
bidders_left = "y"  # Variable to control the bidding loop.


def clear():
    """
    Function to clear the console screen by printing 100 new lines.
    This simulates a screen clear effect.
    """
    print("\n" * 100)


def highest_bidder(auction_bids):
    """
    Function to determine and print the highest bidder.

    Parameters:
    auction_bids (dict): A dictionary containing bidder names as keys and their bid amounts as values.
    """
    winner_bid = 0
    winner_name = ""

    for key in auction_bids:  # Loop through all bidders.
        if auction_bids[key] > winner_bid:  # If the current bid is higher than the stored highest bid:
            winner_bid = auction_bids[key]  # Update the highest bid.
            winner_name = key  # Update the winner's name.

    print(f"The winner is {winner_name} with a bid of ${winner_bid}")  # Announce the winner.


# Start the bidding process.
while bidders_left != "n":  # Continue looping until there are no more bidders.
    print("Welcome to the secret auction program.")
    name = input("Your Name: ").upper()
    bid = int(input("Your Bid: $"))

    auction[name] = bid  # Store the bid in the auction dictionary.

    bidders_left = input("Are there any other bidders? type [y] or [n]").lower()  # Check if more bidders exist.
    clear()  # Clear the screen after each bid to maintain secrecy.

highest_bidder(auction)  # Determine and display the highest bidder after all bids are placed.
