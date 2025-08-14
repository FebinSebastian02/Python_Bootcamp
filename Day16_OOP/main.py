# TODO: Instantiate an object from the inbuilt turtle module
import turtle
from turtle import Screen

# Object = Class()
tim = turtle.Turtle()  # Tim - Name of object
tim.shape("turtle")
tim.color("coral")

my_screen = Screen()
print(my_screen.canvheight)  # canvheight - Class attribute

# TODO: Move the turtle
should_move = True
count = 1

while should_move:
    tim.forward(100)
    tim.left(120)
    count += 1
    if count == 3:
        tim.forward(100)
        should_move = False

my_screen.exitonclick()  # Class method

