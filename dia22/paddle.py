from turtle import Turtle

class Paddle (Turtle): 
    def __init__(self):
        super().__init__()
        
    
    def create_paddle(self,x_position, y_position):
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(x_position,y_position)
        self.color("white")
        self.penup()
        self.speed("fastest")


    def up(self):
        new_y=self.ycor()+50
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y=self.ycor()-50
        self.goto(self.xcor(),new_y)

