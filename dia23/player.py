from turtle import Turtle

from car_manager import CarManager

MOVE_DISTANCE = 50
FINISH_LINE_Y = 280

class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.STARTING_POSITION = (0, -280)
        self.finish_line =FINISH_LINE_Y
        self.restart_position()

    def restart_position(self):
        self.penup()
        self.goto(self.STARTING_POSITION)
        self.setheading(90)
        

    def up(self):
        self.forward(MOVE_DISTANCE)


