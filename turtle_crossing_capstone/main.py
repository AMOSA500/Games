from turtle import Turtle, Screen
from player import Player
from traffic import Cars
import time

# Create the turtle screen
screen = Screen()
screen.title('The Turtle Crossing Capstone Game')
screen.setup(600, 600)
screen.colormode(255)
screen.tracer(0)

# Create a player
player = Player()
traffic = Cars()

# Create screen listener - The turtle only moves forward
screen.listen()
screen.onkey(player.go_up, 'Up')


is_game_on = True
while is_game_on:

    time.sleep(0.1)
    screen.update()
    if traffic.all_cars[-1].xcor() < 250:
        traffic.create_car()
    traffic.move_cars()

    # Collision with the finish line
    if player.ycor() > 290:
        print('Change level')
        player.refresh()

screen.exitonclick()

