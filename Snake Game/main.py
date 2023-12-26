from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.title(titlestring='My Snake Game')
screen.bgcolor('black')
screen.setup(width=500, height=500)
screen.tracer(False)


snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()


screen.exitonclick()