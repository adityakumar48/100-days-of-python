# from turtle import Turtle, Screen

# timmy = Turtle()

# #

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# for _ in range(15):
#     timmy.forward(18)
#     timmy.penup()
#     timmy.forward(18)
#     timmy.pendown()

# number_of_sides = 5


# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

#
# screen = Screen()
# screen.exitonclick()
