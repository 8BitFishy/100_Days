from turtle import Screen
from random import randrange
import time
import snake
import food


screen = Screen()
height = width = 600
screen.setup(height=height, width=width)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

speed = 0.9
snake = snake.Snake()
food = food.Food()
screen.update()
screen.listen()

while True:

    if snake.head.distance(food) < 15:
        food.move_location()
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_down, "Down")


    screen.update()

    time.sleep(speed)
    snake.move()

    speed /= 1.01











screen.exitonclick()