import turtle
import turtle as t
import random

# How to extract the color from an image using COLORGRAM package
# import colorgram
#
# colors = colorgram.extract('img.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
              (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
              (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44),
              (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tur = t.Turtle()
tur.penup()
tur.speed(0)
tur.hideturtle()
tur.setheading(225)
tur.forward(300)
tur.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    tur.dot(20, random.choice(color_list))
    tur.forward(50)

    if dots % 10 == 0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)


screen = t.Screen()
screen.exitonclick()
