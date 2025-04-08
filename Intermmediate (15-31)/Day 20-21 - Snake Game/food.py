from turtle import Turtle
import random

class Food(Turtle):
    """
    Represents the food object in the Snake game.
    Inherits from the Turtle class and randomly moves to a new location when eaten.
    """

    def __init__(self):
        """
        Initializes the food as a small white circle placed at a random position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)  # Slightly smaller than default size
        self.color("white")
        self.speed("fastest")  # Prevents drawing animation delays
        self.refresh()  # Places food at a random position initially

    def refresh(self):
        """
        Moves the food to a new random location within the screen bounds.
        Called when the snake eats the food.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
