from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = 5
MOVE_INCREMENT = 10

class CarManager (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars=[]

    def make_car(self):
        car=Turtle()
        car.penup()
        car.shape("square")
        car.speed("fastest")
        car.color(random.choice(COLORS))
        car.goto(300,random.randint(-200,300))
        car.shapesize(1, 2)
        self.cars.append(car)

    def move(self,speed):
        for car in self.cars:
            car.backward(speed)


    def detect_collition(self,turtle):
        for car in self.cars:
            if car.distance(turtle)<25:
                return True
