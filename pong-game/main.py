from turtle import Screen
from pong import Pong
from ball import Ball
import time
from tkinter import messagebox
from scoreboard import ScoreBoard

# Create Pong screen 800 x 600
screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')
screen.tracer(0)

# Create class Object - default size of paddle is 20x20
r_paddle = Pong((380, 0), 'white')
l_paddle = Pong((-380, 0), 'orange')
ball = Ball()
# centerline = Pong((0, 0), 'white')
# centerline.centerline()
l_score = ScoreBoard((-50, 240))
r_score = ScoreBoard((50, 240))

# Create Paddle movement
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

# Main Game
is_game_on = True
message = messagebox.askyesno('Start Game', 'Play Game Now?')
if message:
    while is_game_on:
        screen.update()
        time.sleep(0.07)
        ball.move()

        # Collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Collision with the paddle
        if ball.distance(r_paddle) < 70 and ball.xcor() > 350:
            ball.bounce_x()
        if ball.distance(l_paddle) < 70 and ball.xcor() < -350:
            ball.bounce_x()

        # Detect if right paddle missed the ball
        if ball.xcor() > 390:  # Right paddle
            l_score.l_display()
            ball.start_point()
        if ball.xcor() < -390:  # Left paddle
            r_score.r_display()
            ball.start_point()

else:
    is_game_on = False
screen.exitonclick()
