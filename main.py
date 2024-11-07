from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the playground

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350, 0)


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_is_on = True

score = Scoreboard()

t = 0.07

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() >= 320 and ball.distance(r_paddle) <= 40 or ball.xcor() <= -320 and ball.distance(l_paddle) <= 40:
        ball.bounce_x()

    if ball.xcor() > 650:
        ball.restart()
        score.l_scoring()

    if ball.xcor() < -650:
        ball.restart()
        score.r_scoring()








screen.exitonclick()
