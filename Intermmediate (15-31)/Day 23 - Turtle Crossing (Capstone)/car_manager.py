from turtle import Turtle
import random

# List of possible colors for the cars
COLORS = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

# Initial speed and how much it increases per level
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    """
     Manages all car-related behavior in the game, including:
     - Creating cars with random colors and positions.
     - Moving cars across the screen.
     - Increasing car speed as levels progress.
     """

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """
        Creates a new car based on a probability that increases as the car speed increases.
        Higher levels mean higher car speed and a greater chance to spawn a car.
        """
        # Calculate spawn chance: higher speed = higher chance to spawn a car
        # The base divisor (6) decreases as speed increases, increasing the spawn rate
        # Make sure divisor stays at least 1 to avoid errors
        spawn_chance_divisor = max(1, int(6 - self.car_speed / 10))

        if random.randint(1, spawn_chance_divisor) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars on screen by their current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increases the speed of the cars for the next level."""
        self.car_speed += MOVE_INCREMENT
