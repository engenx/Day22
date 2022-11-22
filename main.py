from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Ping Pong")
screen.tracer(0)


rpad = Paddle((350, 0))
lpad = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(rpad.go_up, "Up")
screen.onkey(rpad.go_down, "Down")
screen.onkey(lpad.go_up, "w")
screen.onkey(lpad.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(rpad) < 50 and ball.xcor() > 320:
        print("Made contact")
        ball.ret()

    if ball.distance(lpad) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.ret()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

