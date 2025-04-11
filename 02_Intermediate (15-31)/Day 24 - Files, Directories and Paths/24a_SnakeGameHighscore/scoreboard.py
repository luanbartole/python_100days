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
        with open("data.txt") as score_file:
            try:
                self.high_score = int(score_file.read())
            except ValueError:
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)  # Position near the top center of the screen
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clean the previous score and displays the current one on the screen.
        Called after initialization and whenever the score changes.
        """
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score_file:
                score_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     Displays the 'GAME OVER' message in the center of the screen.
    #     """
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the score by 1, and updates it.
        """
        self.score += 1
        self.update_scoreboard()
