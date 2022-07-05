from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard=Scoreboard()
screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


screen.tracer(0)
paddle=Paddle()
paddle2=Paddle()
ball=Ball()
paddle.create_paddle(-350,0)
paddle2.create_paddle(350,0)


screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_on=True
while game_on==True:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart_position()
        scoreboard.p1_point()

    if ball.xcor() < -380:
        ball.restart_position()
        scoreboard.p2_point()

screen.exitonclick()