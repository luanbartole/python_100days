from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random, time

# Color palette used for dynamic paddle and ball color changes
COLOR_LIST = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

# Screen setup
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong by Luan Bartole")
screen.tracer(0)

# Function to randomly change paddle and ball colors
def change_colors(left_paddle, right_paddle, game_ball):
    left_paddle.color(random.choice(COLOR_LIST))
    right_paddle.color(random.choice(COLOR_LIST))
    game_ball.color(random.choice(COLOR_LIST))

# Initialize game objects
ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Apply initial random colors
change_colors(left_paddle=l_paddle, right_paddle=r_paddle, game_ball=ball)

# Event listeners for paddle control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # Detect collision with paddles
    current_time = time.time()
    if (
        current_time - ball.last_paddle_hit_time > 1 and  # cooldown check
        ((ball.distance(r_paddle) < 60 and ball.xcor() > 320) or
         (ball.distance(l_paddle) < 60 and ball.xcor() < -320))
    ):
        ball.bounce("x")
        ball.increase_speed()
        l_paddle.increase_speed()
        r_paddle.increase_speed()

    # Detect when a paddle misses and update score
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() < 0:
            scoreboard.increase_score("right")
        if ball.xcor() > 0:
            scoreboard.increase_score("left")

        # Reset ball and paddles
        ball.reset_position()
        l_paddle.pspeed = 20
        r_paddle.pspeed = 20
        change_colors(left_paddle=l_paddle, right_paddle=r_paddle, game_ball=ball)

# Close game on click
screen.exitonclick()
