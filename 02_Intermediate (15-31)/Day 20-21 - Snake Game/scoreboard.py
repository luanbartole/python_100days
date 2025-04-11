from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    """
    Represents the scoreboard in the Snake game.
    Inherits from Turtle and handles displaying and updating the player's score.
    """

    def __init__(self):
        """
        Initializes the scoreboard at the top of the screen and sets the starting score to 0.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)  # Position near the top center of the screen
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Displays the current score on the screen.
        Called after initialization and whenever the score changes.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Displays the 'GAME OVER' message in the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score by 1, clears the old score display, and updates it.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
