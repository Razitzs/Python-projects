import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
screen=Screen()
t.colormode(255)

def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    a=(r,g,b)
    return a

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(randomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))
screen.exitonclick()

