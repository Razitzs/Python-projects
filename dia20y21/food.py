from turtle import Turtle
import random 
colors = ['cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange',"light pink2",'yellow']
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.changeLocation()

    def changeLocation(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))

