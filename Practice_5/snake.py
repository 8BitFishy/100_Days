from turtle import Turtle

STARTING_POSITIONS = [[0, 0], [-20, 0], [-40, 0]]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = self.initialise()
        self.head = self.segments[0]

    def initialise(self):
        segments = []
        positions = STARTING_POSITIONS

        for position in positions:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setposition(position)
            segments.append(snake)
            snake.speed(0)

        return segments

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)
        return

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        return

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        return

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        return

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        return
