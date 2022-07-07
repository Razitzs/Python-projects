import time
from turtle import Screen
from player import Player
from car_manager import CarManager,SPEED,MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle=Player()
scoreboard=Scoreboard(-80,260)
game_over=Scoreboard(-80,0)
screen.listen()

screen.onkey(turtle.up, "Up")
times=0
cars=CarManager()
scoreboard.print_message(scoreboard.xcor(),scoreboard.ycor(),f"Level: {scoreboard.level}")

while True:
    time.sleep(0.1)
    screen.update()

    if times%5==0:
        cars.make_car()
    cars.move(SPEED)

    if turtle.ycor()>=turtle.finish_line:
        time.sleep(1)
        turtle.restart_position()
        scoreboard.level+=1
        scoreboard.print_message(scoreboard.xcor(),scoreboard.ycor(),f"Level: {scoreboard.level}")
        SPEED+=MOVE_INCREMENT

    if cars.detect_collition(turtle)==True:
        game_over.print_message(game_over.xcor(),game_over.ycor(),"GAME OVER")
        break

    times+=1


screen.exitonclick()