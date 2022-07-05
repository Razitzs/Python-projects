from turtle import Turtle, Screen, color
import random
screen= Screen()
colors = ['cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange',"light pink2",'yellow']
yPositions=[-100,-70,-40,-10,20,50]
screen.setup(width=500,height=400)

def initialize(colors,i):
    turtle=Turtle(shape="turtle")
    turtle.penup()
    turtle.color(i)
    return turtle

raceStarted=False
userBet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if userBet:
    raceStarted=True

turtles=[]
for i in range (6):
    color=colors[i]
    t=initialize(colors,color)
    t.goto(x=-230,y=yPositions[i])
    turtles.append(t)

while raceStarted==True:
    for turtle in turtles:
        if turtle.xcor() > 230:
            raceStarted=False
            winningColor=turtle.pencolor()
            if winningColor==userBet:
                print(f"You've won! The {winningColor} turtle is the winner!")
            else:
                print(f"You've lost! The {winningColor} turtle is the winner!")
        distance=random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()