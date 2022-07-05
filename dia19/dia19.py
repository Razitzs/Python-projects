from turtle import Turtle, Screen

tim=Turtle()
screen= Screen()

def moveForwards():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def turnLeft():
    tim.left(10)

def turnRight():
    tim.right(10)

def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(moveForwards,"w")
screen.onkey(moveBackwards,"s")
screen.onkey(turnLeft,"a")
screen.onkey(turnRight,"d")
screen.onkey(clearScreen,"c")
screen.exitonclick()