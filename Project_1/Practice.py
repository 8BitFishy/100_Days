import turtle as t
from random import randrange, choice
import colorgram

tim = t.Turtle()
tim.speed(5)
tim.shape("turtle")
tim.hideturtle()
print("Extracting colours")
colours = colorgram.extract(('image.jpg'), 25)
print("colors extracted")
tim.pensize(100)
tim.penup()
tim.setpos(-250, -250)


for row in range(5):
    for col in range(5):
        tim.pendown()
        colour = choice(colours)
        tim.pencolor((colour.rgb[0] / 255, colour.rgb[1] / 255, colour.rgb[2] / 255))
        tim.forward(1)
        tim.penup()
        if col != 4:
            tim.forward(150)

    if row % 2 == 0:
        tim.left(90)
        tim.forward(150)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(150)
        tim.right(90)

screen = t.Screen()
screen.exitonclick()