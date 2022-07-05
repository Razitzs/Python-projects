from turtle import Turtle
import random 
class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.x_speed=.3
        self.y_speed=.3
        self.speed=0.3


    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.speed *= 1

    def restart_position(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()


