from turtle import Turtle

# Font style used for displaying text on the screen
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    """
    A scoreboard that displays the current level and shows 'Game Over' when the game ends.
    Inherits from the Turtle class to write directly on the screen.
    """

    def __init__(self):
        """
        Initializes the scoreboard, sets the starting level to 1,
        and displays the initial level text.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Top-left corner for level display

        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and rewrites the current level on the screen."""
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increases the level by 1 and updates the display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays 'GAME OVER' at the center of the screen."""
        self.goto(-80, 0)
        self.write("GAME OVER", align="left", font=FONT)
