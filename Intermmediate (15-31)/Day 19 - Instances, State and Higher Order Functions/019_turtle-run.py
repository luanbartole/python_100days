from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(500, 400)  # Width=500, Height=400
turtles = []  # List to store all turtle racers

# --- Function to create and position turtles ---
def turtle_setup(turtle_list):
    color_list = ["red", "green", "blue", "purple", "orange", "gold"]  # Colors for each turtle
    y_axis = -75  # Starting vertical position

    for color in color_list:
        new_turtle = Turtle(shape="turtle")  # Create a turtle with the "turtle" shape
        new_turtle.color(color)              # Set turtle color
        new_turtle.penup()                   # Lift pen to avoid drawing lines
        new_turtle.goto(x=-230, y=y_axis)    # Place turtle at the left starting line
        turtle_list.append(new_turtle)       # Add turtle to the list
        y_axis += 30                         # Move the next turtle up vertically

# --- Function to start the race ---
def turtle_run(turtle_list):
    while True:
        for turtle in turtle_list:
            steps = random.randint(5, 25)    # Random movement step size
            turtle.forward(steps)            # Move the turtle forward
            if turtle.xcor() >= 250:         # Check if turtle reached finish line
                return turtle.color()        # Return the color of the winning turtle


# Ask the user to place a bet
user_bet = screen.textinput(
    "Turtle Run",
    "Which turtle will be the winner?\n\n[red] [green] [blue] [purple] [orange]:\n"
)

# Set up the turtles and start the race
turtle_setup(turtles)
winner = turtle_run(turtles)  # Get the winner's color

# Display race results to the user
if user_bet == winner[0]:
    print(f"Congratulations! The [{winner[0]}] turtle won!")
else:
    print(f"You lost! The [{winner[0]}] turtle won!")

# Wait for user to click on the screen before closing
screen.exitonclick()
