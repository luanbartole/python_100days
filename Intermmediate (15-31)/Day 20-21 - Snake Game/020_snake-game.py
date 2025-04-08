from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Luan Bartole")
screen.tracer(0)  # Turn off automatic animation

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.09)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail (self-collision)
    for segment in snake.segments[1:]:  # Skip the head itself
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Wait for a click before closing the window
screen.exitonclick()
