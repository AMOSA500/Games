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
paddle.goto(350,0)


screen.exitonclick()