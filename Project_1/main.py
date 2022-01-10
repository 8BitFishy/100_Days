from turtle import Turtle, Screen
import random
import math

pred_turtle = Turtle()
prey_turtle = Turtle()

turtle_list = [pred_turtle, prey_turtle]

bounds = [500, 500]
pred_turtle.name = "pred"
pred_turtle.shape("turtle")
pred_turtle.color("red")
pred_turtle.angle = 0
prey_turtle.name = "prey"
prey_turtle.shape("turtle")
prey_turtle.color("blue")
prey_turtle.angle = 0

prey_turtle.forward(10)
print(pred_turtle.pos())


def Trig(move):

    #if run = 0 and rise is
    if move[0] == 0 and move[1] != 0:
        #greater than 0
        if move[1] > 0:
            #angle is 90
            move_angle = 90
        #less than 0
        else:
            #angle is -90
            move_angle = -90

    #if rise is 0 and run is
    elif move[0] != 0 and move[1] == 0:
        #greater than 0
        if move[0] > 0:
            #angle is 90
            move_angle = 0
        #less than 0
        else:
            #angle is 90
            move_angle = 180

    #if neither value is 0
    else:
        #calculate angle from 0
        move_angle = abs(math.degrees(math.atan(move[1] / move[0])))
        print(f"Angle from 0 is {move_angle}")

        if move[1] > 0 and move[0] > 0:
            print("rise positive, run positive")
            move_angle = 0-move_angle

        elif move[1] > 0 and move[0] < 0:
            print("rise positive, run negative")
            move_angle = 180 + move_angle

        elif move[1] < 0 and move[0] < 0:
            print("rise negative, run negative")
            move_angle = 180 - move_angle

        else:
            print("rise negative, run positive")
            move_angle = move_angle

    print(f"Returned angle = {move_angle}")
    return move_angle

def Generate_Movement(turtle, move):
    if move[0] == 0 and move[1] == 0:
        move_angle = 0
        move_length = 0

    else:
        move_angle = Trig(move)
        move_length = math.sqrt((move[0] * move[0]) + (move[1] * move[1]))

    print(f"new_angle = {move_angle} - {turtle.angle}")
    new_angle = move_angle - turtle.angle
    turtle.angle = move_angle

    print(f"Move length = {move_length}")
    print(f"New angle = {new_angle}")
    '''
    if new_angle > 180:
        turtle.left(new_angle - 180)
    elif new_angle < -180:
        turtle.right(-180 - new_angle)
    else:
        turtle.right(new_angle)
'''
    Generate_Angle(turtle, new_angle)
    Move_Turtle(turtle, move_length)

    return turtle


def Move_Turtle(turtle, move_length):
    turtle.forward(move_length)
    return turtle

def Generate_Angle(turtle, new_angle):
    if new_angle > 180:
        turtle.left(new_angle - 180)
    elif new_angle < -180:
        turtle.right(-180 - new_angle)
    else:
        turtle.right(new_angle)
    return turtle

for i in range(5):
    for turtle in turtle_list:
        if turtle.name == 'prey':
            turtle.forward(100)
            continue
        else:
            print()
            print(f"moving {turtle.name} from position {turtle.pos()} at angle {turtle.angle}")
            move = []
            for i in range(2):
                move.append(random.randint(-100, 100))
            print(f"New move {move}")
            turtle = Generate_Movement(turtle, move)

            print(f"New position = {turtle.pos()}")
            print("______________________________________")












screen = Screen()
screen.exitonclick()