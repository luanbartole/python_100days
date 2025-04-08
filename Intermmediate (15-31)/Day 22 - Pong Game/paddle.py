from turtle import Turtle

MAX_PSPEED = 40  # Maximum paddle speed


class Paddle(Turtle):
    """
    Represents a paddle in the Pong game.
    """

    def __init__(self, coordinates):
        """
        Initializes the paddle with a starting position and base speed.

        Args:
            coordinates (tuple): Starting (x, y) position of the paddle.
        """
        super().__init__()
        self.start_x = coordinates[0]
        self.start_y = coordinates[1]
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Makes the paddle tall and narrow
        self.color("white")
        self.penup()
        self.goto(self.start_x, self.start_y)
        self.pspeed = 20  # Initial paddle speed

    def go_up(self):
        """
        Moves the paddle upward by its current speed.
        """
        new_y = self.ycor() + self.pspeed
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the paddle downward by its current speed.
        """
        new_y = self.ycor() - self.pspeed
        self.goto(self.xcor(), new_y)

    def increase_speed(self):
        """
        Increases the paddle's movement speed, up to the defined maximum.
        """
        if self.pspeed < MAX_PSPEED:
            self.pspeed += 2
            if self.pspeed > MAX_PSPEED:
                self.pspeed = MAX_PSPEED  # Clamp to max speed
