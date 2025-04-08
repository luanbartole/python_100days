from turtle import Turtle
import random

# Constants for movement directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# A list of RGB colors to randomly color the snake's segments
COLOR_LIST = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]


class Snake:
    """
    Represents the snake in the game. Handles movement, growth, and direction changes.
    """

    def __init__(self):
        """
        Initializes the snake with a default length and sets its head.
        """
        self.segments = []
        self.initial_body_segments = 3
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")  # Distinct shape for the head

    def create_snake(self):
        """
        Creates the initial segments of the snake and positions them.
        """
        x_axis = 0
        for body_part in range(self.initial_body_segments):
            self.add_segment()
            x_axis -= 20  # (This value isn't currently used but could represent spacing)

    def add_segment(self):
        """
        Adds a new segment to the snake at the current x=0.
        Used for both initial creation and growth when eating food.
        """
        x_axis = 0
        segment = Turtle(shape="square")
        segment.color(random.choice(COLOR_LIST))  # Random color for visual flair
        segment.penup()
        segment.setx(x_axis)
        self.segments.append(segment)

    def move_snake(self):
        """
        Moves the snake forward by shifting each segment to the position
        of the one ahead of it. The head moves forward in its current direction.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        """
        Changes direction to up if not currently going down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes direction to down if not currently going up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes direction to left if not currently going right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes direction to right if not currently going left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
