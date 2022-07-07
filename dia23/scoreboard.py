from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard (Turtle):
    def __init__ (self,xcor,ycor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(xcor,ycor)
    
    def print_message(self,xcor,ycor,message):
        self.clear()
        self.write(f"{message}", move=False, align='left', font=FONT)

    
