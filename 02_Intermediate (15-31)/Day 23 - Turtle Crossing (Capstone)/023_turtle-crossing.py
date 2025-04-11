import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create game objects
player = Player()
screen = Screen()
screen.title("Turtle Crossing by Luan Bartole")
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up the screen
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Listen for player input
screen.listen()
screen.onkey(player.move_up, "Up")  # Move the player up when the "Up" arrow key is pressed

# Start the main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Add a short delay to control the game speed
    screen.update()  # Update the screen manually

    # Create new cars and move all existing cars
    car_manager.create_cars()
    car_manager.move_cars()

    # Check for collisions between the player and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Check if the player reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()       # Reset player to starting position
        car_manager.level_up()     # Increase game difficulty (e.g., car speed)
        scoreboard.increase_level()

# Keep the window open until clicked
screen.exitonclick()
