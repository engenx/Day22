from turtle import Screen, Turtle
import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Ping Pong")
screen.tracer(0)

rpad = Paddle((350, 0))
lpad = Paddle((-350, 0))


def go_up():
    new_y = rpad.ycor() + 20
    rpad.goto(rpad.xcor(), new_y)


def go_down():
    new_y = rpad.ycor() - 20
    rpad.goto(rpad.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()