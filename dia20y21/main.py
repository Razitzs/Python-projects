from turtle import Screen
from snake import Snake
from food import Food,colors
from scoreboard import Scoreboard
import time
import random

scoreboard=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
food=Food()
snake = Snake()
snake.createSnake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

loose=False
while loose!=True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.write(f"Score: {scoreboard.score}", move=False, align='left', font=('Courier', 24, 'normal'))
    
    if snake.turtles[0].xcor()>290 or snake.turtles[0].xcor()<-290 or snake.turtles[0].ycor()>290 or snake.turtles[0].ycor()<-290:
        sc=scoreboard.endGame()
        loose=True

    if snake.turtles[0].distance(food)<15:
        scoreboard.updateScore()
        food.changeLocation()
        food.color(random.choice(colors))
        snake.grow()
    
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle)<10:
            sc=scoreboard.endGame()
            loose=True

screen.exitonclick()