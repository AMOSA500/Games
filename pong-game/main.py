from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game')

# Create a paddle
paddle = Turtle('square')
paddle.penup()
paddle.color('white')
paddle.shapesize(stretch_len=20, stretch_wid=100)
paddle.goto(0,0)


screen.exitonclick()