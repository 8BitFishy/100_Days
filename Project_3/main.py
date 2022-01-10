from turtle import Turtle, Screen
from itertools import count
from random import randrange


turtle_count = 7


class Turtles():
    _ids = count(0)
    def __init__(self, colour, speed, start_position):
        self.id = next(self._ids)
        self.turtle = Turtle()
        self.colour = colour
        self.speed = speed
        self.start_position = start_position

    def initialise_turtle(self):
        self.turtle.shape("turtle")
        self.turtle.turtlesize(10/turtle_count)
        self.turtle.speed(0)
        self.turtle.color(self.colour)
        self.turtle.penup()
        self.turtle.setposition(self.start_position[0]-20, self.start_position[1])
        self.label()
        self.turtle.forward(20)
        self.turtle.speed(1)
        self.turtle.pendown()




    def move(self, distance):
        self.turtle.forward((self.speed * distance) / 2)

    def check_for_winner(self):
        if self.turtle.position()[0] >= 500:
            return True
        else:
            return False

    def find_position(self):
        return self.turtle.pos()[0]

    def label(self):
        self.turtle.write(f"{self.id + 1}", False, align = "right", font = 15)


def draw_field(position, turtle_count, spread):
    box_turtle = Turtle()
    box_turtle.hideturtle()
    box_turtle.speed(0)
    box_turtle.penup()
    box_turtle.setposition(position[0], position[1]+50)
    box_turtle.pendown()
    box_turtle.forward(1000)
    box_turtle.right(90)
    box_turtle.forward((turtle_count-1) * spread + 100)
    box_turtle.right(90)
    box_turtle.forward(1000)
    box_turtle.right(90)
    box_turtle.forward((turtle_count-1) * spread + 100)
    return


def get_user_bet():
    return screen.textinput(title = "Place Your Bet!", prompt="Which turtle do you think will win?")


if __name__ == '__main__':

    screen = Screen()
    height = 1000
    screen.setup(width=1250, height=height)
    spread = 1000/turtle_count
    print(spread)

    turtle_list = []
    for i in range(turtle_count):
        colour = (randrange(0, 255) / 255, randrange(0, 255) / 255, randrange(0, 255) / 255)
        speed = randrange(10, 15)
        range = (turtle_count-1) * spread
        start_position = [-500, i*spread - range/2]
        turtle = Turtles(colour, speed, start_position)
        turtle.initialise_turtle()
        turtle_list.append(turtle)
        print(f"turtle {turtle.id + 1} at {start_position}")



    draw_field(start_position, turtle_count, spread)

    bet = get_user_bet()

    Winner = False


    print("\n\nStarting")
    leader = 0
    leader_position = -500



    while Winner == False:
        for turtle in turtle_list:
            roll = randrange(1, 3)
            turtle.move(roll)
            position = turtle.find_position()

            if turtle.check_for_winner():
                Winner_id = turtle.id
                Winner = True
                break

            if position > leader_position:
                leader_position = position
                leader = turtle.id
        print(f"Turtle {leader + 1} currently in the lead")

    turtle.label()
    print(f"\n\nThe winner was:\nTurtle {Winner_id+1}!")
    print(f"You bet on {bet}")
    if bet == Winner_id:
        print("You won!")
    else:
        print("You lost, better luck next time loser...")



    screen.exitonclick()



