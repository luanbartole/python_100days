from turtle import Turtle

# Constants for the player's starting position, move distance, and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Represents the player-controlled turtle that moves upward across the screen.
    Inherits from the Turtle class in the turtle module.
    """

    def __init__(self):
        """Initializes the player turtle at the starting position and facing upward."""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)  # Make the turtle face upward

    def move_up(self):
        """Moves the turtle forward by a fixed distance."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """
        Checks if the player has crossed the finish line.

        Returns:
            bool: True if the turtle has reached or passed the top of the screen.
        """
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        """Moves the turtle back to the starting position."""
        self.goto(STARTING_POSITION)
