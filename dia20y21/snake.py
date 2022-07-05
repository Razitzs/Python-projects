from turtle import Turtle

xPositions=[0,-20,-40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.turtles=[]

    def initialize(self,xposition, yposition):
        turtle=Turtle(shape="square")
        turtle.goto(xposition,yposition)
        turtle.color("white")
        turtle.penup()
        turtle.speed("fastest")
        self.turtles.append(turtle)

    def createSnake(self):
        for i in xPositions:
            self.initialize(i,0)
            
    def move(self):
        for turtle in range(len(self.turtles)-1,0,-1):
            newX=self.turtles[turtle-1].xcor()
            newY=self.turtles[turtle-1].ycor()
            self.turtles[turtle].goto(newX,newY)
        self.turtles[0].forward(20)

    def grow(self):
        self.initialize(self.turtles[-1].xcor(),self.turtles[-1].ycor())

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

