from turtle import Turtle

class Egg(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

        # Move self
    def move(self):
       
        ball_y = self.ycor() + self.y_move
        ball_x = self.xcor() + self.x_move
        self.goto(ball_x,ball_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_ball_pos(self):
        self.goto(0,0)
        self.bounce_x()
        
            