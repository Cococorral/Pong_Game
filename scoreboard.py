from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def r_scoring(self):
        self.clear()
        self.r_score += 1
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_scoring(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))


