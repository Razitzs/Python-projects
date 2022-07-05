import colorgram
import turtle
import random
from turtle import Screen

turtle.colormode(255)
t = turtle.Turtle()
screen=Screen()
turtle.colormode(255)
t.speed("fastest")
t.width(10)
colors = colorgram.extract('C:\Cosas que sí ocupo\Cursos\Python Bootcamp\Días\dia18\image.jpg', 30)

rgb=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    newColor=(r,g,b)
    rgb.append(newColor)

t.hideturtle()
t.penup()
t.setheading(255)
t.forward(300)
t.setheading(0)

for i in range (1,11):
    for j in range (9):
        t.color(random.choice(rgb))
        t.dot()
        t.forward(50)
        t.dot()
    if i%2!=0:
        t.left(90)
        t.forward(50)
        t.left(90)
    else:
        t.right(90)        
        t.forward(50)
        t.right(90)

screen.exitonclick()