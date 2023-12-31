from turtle import  Screen
from player import Player
from traffic import Cars
from scoreboard import Scoreboard
import time

# Create the turtle screen
screen = Screen()
screen.title('The Turtle Crossing Capstone Game')
screen.setup(600, 600)
screen.colormode(255)
screen.tracer(0)

# Create a player
player = Player()
car = Cars()
level = Scoreboard()

# Create screen listener - The turtle only moves forward
screen.listen()
screen.onkey(player.go_up, 'Up')


is_game_on = True
while is_game_on:

    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # Collision with the finish line
    if player.is_at_finish_point():
        car.increase_speed()
        level.next_level()
        player.go_to_start()

    # Detect Collision with Cars
    for vehicle in car.all_cars:
        if player.distance(vehicle) < 20:
            level.game_over()
            is_game_on = False

screen.exitonclick()

