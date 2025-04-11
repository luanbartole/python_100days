import art 


n1 = 0 
n2 = 0 
endprogram = False  


def line(number):
    """
    Function to print a separator line of a given length.

    Parameters:
    number (int): The number of '=' characters to print.
    """
    print("=" * number)


def calculator(x, y, mode):
    """
    Function to perform basic arithmetic operations.

    Parameters:
    x (float): First number.
    y (float): Second number.
    mode (int): Operation mode (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).

    Returns:
    float: The result of the operation, or None if an invalid mode is passed.
    """
    if mode == 1:
        return x + y  # Addition
    elif mode == 2:
        return x - y  # Subtraction
    elif mode == 3:
        return x * y  # Multiplication
    elif mode == 4:
        return x / y  # Division
    else:
        print("You have passed the wrong parameters.")
        return None  # Return None if an invalid operation is selected.


print(art.logo)  # Display the logo.

while not endprogram:  # Loop until the user decides to quit.

    line(25)  

    # Prompt user for numbers, only ask for the first number if it's not stored from previous calculation.
    if n1 == 0:
        n1 = float(input("First Number: "))
    n2 = float(input("Second Number: "))

    line(25)

    # Display available operations.
    print("Operations:\n[1] Addition \n[2] Subtraction \n[3] Multiplication \n[4] Division")

    line(25)

    op = int(input("Choose your Operation: "))  # Get user operation choice.

    n3 = calculator(n1, n2, op)  # Perform the calculation.

    print(f"The result is: {n3:.2f}")  # Display the result formatted to two decimal places.

    line(25)
    print()

    # Ask user if they want to continue.
    if input("Would you like to do another calculation? [Y] or [N]? ").upper() == "N":
        endprogram = True  # Exit loop if user chooses 'N'.
    else:
        # Ask if the user wants to continue using the last result as the first number.
        reuse_number = input(f"Keep calculating with {n3}? [Y] or [N]? ").upper()
        if reuse_number == "N":
            n1 = 0  # Reset first number if user chooses 'N'.
        elif reuse_number == "Y":
            n1 = n3  # Keep using the last result if user chooses 'Y'.
        else:
            line(25)
            print("You have typed something random, haven't you? This is what you get!")
            line(25)
            endprogram = True  # End program on invalid input.

    print()
