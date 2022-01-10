from turtle import  Turtle, Screen


tim = Turtle()

screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)
    return

def move_back():
    tim.backward(10)
    return

def turn_left():
    print(tim.heading())
    tim.setheading(tim.heading() + 10)
    print(tim.heading())
    return

def turn_right():
    tim.setheading(tim.heading() - 10)
    return

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    return

screen.onkey(move_forward, "Up")
screen.onkey(move_back, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")



screen.exitonclick()