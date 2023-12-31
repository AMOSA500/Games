from turtle import Turtle, Screen
from player import Player
import time

# Create the turtle screen
screen = Screen()
screen.title('The Turtle Crossing Capstone Game')
screen.setup(600, 600)
screen.colormode(255)
screen.tracer(0)

# Create a player
player = Player()

# Create screen listener
screen.listen()
screen.onkey(player.go_up, 'Up')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()

