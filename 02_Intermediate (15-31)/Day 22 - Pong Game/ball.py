import time
from turtle import Turtle

# Constants
MOVE_DISTANCE = 10
MAX_BSPEED = 0.028  # Fastest speed the ball can reach (lower value = faster movement)


class Ball(Turtle):
    """
    Represents the ball in the Pong game. Handles movement, bouncing, speed increase,
    and resetting its position.
    """

    def __init__(self):
        """
        Initializes the ball with shape, color, speed, direction, and starting position.
        """
        super().__init__()
        self.shape("circle")
        self.speed("fastest")  # Drawing speed of the turtle, not related to ball movement delay
        self.color("white")
        self.penup()
        self.bspeed = 0.06  # Delay between movements; controls game speed (higher = slower)
        self.x_move = MOVE_DISTANCE  # Movement in x-axis per step
        self.y_move = MOVE_DISTANCE  # Movement in y-axis per step
        self.last_paddle_hit_time = time.time()  # Cooldown timer to avoid double-bounce

    def move_ball(self):
        """
        Moves the ball forward by its current x and y direction.
        Uses sleep to control the ball speed based on bspeed.
        """
        time.sleep(self.bspeed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, direction):
        """
        Reverses the direction of the ball based on collision.

        Args:
            direction (str): "x" for horizontal bounce, "y" for vertical bounce
        """
        if direction == "y":
            self.y_move *= -1
        if direction == "x":
            self.x_move *= -1
            self.last_paddle_hit_time = time.time()  # Update cooldown timer

    def increase_speed(self):
        """
        Speeds up the ball by reducing the delay (`bspeed`), but not beyond MAX_BSPEED.
        """
        if self.bspeed > MAX_BSPEED:
            self.bspeed *= 0.9  # Gradual speed increase
            if self.bspeed < MAX_BSPEED:
                self.bspeed = MAX_BSPEED  # Cap the speed to prevent it from going too fast

    def reset_position(self):
        """
        Resets the ball to the center and restores initial speed.
        Reverses direction to give variation.
        """
        self.goto(0, 0)
        self.bspeed = 0.06
        self.bounce("x")
