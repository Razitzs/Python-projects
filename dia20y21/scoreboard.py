from turtle import Turtle

class Scoreboard (Turtle):
    score=0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-80,250)
        self.color("white")
        

    def updateScore(self):
        self.clear()
        self.score+=1

    def endGame(self):
        sc=Scoreboard()
        sc.goto(-180,0)
        sc.write(f"GAME OVER", move=False, align='left', font=('Courier', 50, 'normal'))
        return sc
