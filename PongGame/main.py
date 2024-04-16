from turtle import Turtle, Screen
from paddle import Paddle

# Use of virtual environment - python -m venv myenv, then myenv/Script/activate.bat
# Create a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("Pong Game")
screen.tracer(0) # Turn off animation display on screen

# Create a Paddle
paddle_right = Paddle(370,"blue")
paddle_left = Paddle(-370,"red")

#create a ball
ball = Turtle()
ball.color("orange")
ball.shape("circle")
ball.shapesize(1,1)

# Move ball
ball.penup()
ball.goto(360,300)


    
# Move Paddle up 
screen.listen()
screen.onkey(oago_up,"Up")
screen.onkey(go_down,"Down")

while(True):
    screen.update()
    
screen.exitonclick()