from turtle import Screen, Turtle, forward
import random

timmy=Turtle()
screen=Screen()
timmy.shape("turtle")
colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange',"light pink2"]
veces=3
timmy.width(4)
for j in range (8):
    i=0
    timmy.color(colors[j])
    while(i<veces):
        timmy.forward(100)
        timmy.right(360/veces)
        i+=1
    veces+=1

screen.exitonclick()