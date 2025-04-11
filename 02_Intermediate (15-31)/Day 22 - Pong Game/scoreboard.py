from turtle import Turtle

class Scoreboard(Turtle):
    """
    Displays and manages the score for both players in the Pong game.
    """

    def __init__(self):
        """
        Initializes the scoreboard: hides the turtle, sets color, position, and starts scores at 0.
        """
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.refresh()

    def refresh(self):
        """
        Clears the previous scores and updates them on the screen.
        Left score is shown on the left side, right score on the right side.
        """
        self.clear()
        # Draw left player's score
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Arial", 40, "bold"))

        # Draw right player's score
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Arial", 40, "bold"))

    def increase_score(self, player):
        """
        Increments the score for the specified player and refreshes the display.

        Args:
            player (str): Either "left" or "right", indicating which player's score to increase.
        """
        if player == "left":
            self.left_score += 1
        if player == "right":
            self.right_score += 1
        self.refresh()
