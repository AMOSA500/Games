from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')
screen.tracer(0)

# Create a paddle - default size is 20x20
paddle = Turtle('square')
paddle.penup()
paddle.color('white')
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.goto(350, 0)


def go_up():
    new_ycor = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_ycor)


def go_down():
    new_ycor = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_ycor)


# Create Paddle movement
screen.listen()
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')

# Main Game
is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
