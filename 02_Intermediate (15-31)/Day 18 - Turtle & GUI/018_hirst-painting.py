# List of RGB color tuples used to paint the dots
color_list = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

from turtle import Turtle, Screen
import random

# Create the Turtle object that will act as the paintbrush
paintbrush = Turtle()
paintbrush.pensize(10)        # Set the size of the lines (not really used since we're drawing dots)
paintbrush.speed("fastest")   # Max speed for fast drawing

# Set up the screen with RGB color mode
screen = Screen()
screen.colormode(255)         # Allows using RGB tuples for colors (0–255)

# Position the paintbrush at the starting location
paintbrush.penup()
paintbrush.setpos(-250, -200)  # Bottom-left starting point
paintbrush.pendown()

# --- Function to draw a single colored dot ---
def draw_dot():
    paintbrush.pendown()  # Make sure the pen is down to draw
    random_color = random.choice(color_list)  # Pick a random color from the list
    paintbrush.dot(20, random_color)  # Draw a dot of diameter 20

# --- Function to draw a horizontal line of 10 dots ---
def draw_line(dots=10):
    for _ in range(dots):
        draw_dot()               # Draw one dot
        paintbrush.penup()       # Lift the pen to avoid drawing a line between dots
        paintbrush.forward(50)   # Move forward to space the dots

# --- Function to move up and change direction to begin a new line ---
def change_direction(way):
    paintbrush.setheading(90)   # Point upwards
    paintbrush.penup()
    paintbrush.forward(50)      # Move up to the next row
    paintbrush.pendown()

    # Turn left or right depending on the current row
    if way == "left":
        paintbrush.setheading(180)  # Face left
    if way == "right":
        paintbrush.setheading(0)    # Face right

    paintbrush.penup()
    paintbrush.forward(50)      # Small forward step before starting the next line

# --- Function to draw the full Hirst painting ---
def hirst_painting(line_number):
    counter = 0
    while counter < line_number:
        draw_line()  # Draw one line of dots

        # Change direction depending on whether it's an even or odd line
        if counter % 2 == 0:
            change_direction("left")   # Even lines go left
        if counter % 2 != 0:
            change_direction("right")  # Odd lines go right

        counter += 1  # Move to the next line

# Call the function to draw a painting with 10 rows
hirst_painting(10)

# Hide the paintbrush turtle by setting it to white (invisible on white background)
paintbrush.color("white")

# Keeps the window open until clicked
screen.exitonclick()
