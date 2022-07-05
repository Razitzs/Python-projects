import turtle
import random
from turtle import Screen

t = turtle.Turtle()
screen=Screen()
turtle.colormode(255)
t.speed("fastest")

def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    a=(r,g,b)
    return a

for i in range (80):
    t.color(randomColor())
    t.circle(100)
    t.right(5)

screen.exitonclick()