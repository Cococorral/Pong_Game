from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        current_y = self.ycor()
        self.sety(current_y + 20)

    def down(self):
        current_y = self.ycor()
        self.sety(current_y - 20)
