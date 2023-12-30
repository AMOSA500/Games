from turtle import Screen, Turtle
from pong import Pong
from ball import Ball
import time

# Create Pong screen 800 x 600
screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')
screen.tracer(0)

# Create a paddle - default size is 20x20
r_paddle = Pong((350, 0),'white')
l_paddle = Pong((-350, 0),'orange')
ball = Ball()

# Create Paddle movement
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

# Main Game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.5)
    if ball.ycor() < 300 or ball.ycor() > -300:
        ball.move()

screen.exitonclick()
