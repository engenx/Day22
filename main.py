from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Ping Pong")
screen.tracer(0)


rpad = Paddle((350, 0))
lpad = Paddle((-350, 0))


screen.listen()
screen.onkey(rpad.go_up, "Up")
screen.onkey(rpad.go_down, "Down")
screen.onkey(lpad.go_up, "w")
screen.onkey(lpad.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()

