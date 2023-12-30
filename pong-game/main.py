from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')

# Create a paddle
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
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

screen.exitonclick()
