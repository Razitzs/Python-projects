from turtle import Turtle, Screen, turtles
import time

def initialize():
    turtle=Turtle(shape="square")
    turtle.penup()
    turtle.speed("fastest")
    turtle.color("white")
    return turtle

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snakeeeezzzzzzz")
xPositions=[0,-20,-40]
screen.tracer(0)

turtles=[]
for i in range (0,3):
    turtle=initialize()
    turtle.goto(xPositions[i],y=0)
    turtles.append(turtle)

screen.update()
while True:
    screen.update() #Actualizo la pantalla una vez que los tres cuadros ya se movieron
    time.sleep(0.1)
    for turtle in range(len(turtles)-1,0,-1):
        newX=turtles[turtle-1].xcor()
        newY=turtles[turtle-1].ycor()
        turtles[turtle].goto(newX,newY)
    turtles[0].forward(20)
        







screen.exitonclick()