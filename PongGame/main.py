from turtle import Screen
from paddle import Paddle
from egg import Egg
import time

# Use of virtual environment - python -m venv myenv, then myenv/Script/activate.bat
# Create a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # Turn off animation display on screen

# Create a Paddle
paddle_right = Paddle((370,0),"blue")
paddle_left = Paddle((-370,0),"red")

#create a ball
ball = Egg()


    
# Move Paddle up 
screen.listen()
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

while(True):
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #
    
screen.exitonclick()