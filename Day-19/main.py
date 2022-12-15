from turtle import Turtle, Screen

tin = Turtle()
screen = Screen()


def move_forwards():
    tin.forward(10)


def move_backwards():
    tin.backward(10)


def turn_left():
    tin.left(10)


def turn_right():
    tin.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.exitonclick()
