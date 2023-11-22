# Cookies
# Author:
# 21 November 2023

import random
import turtle


# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")

# Design a function that creates a cookie at x and y
def make_cookie(x: int, y: int):
    """Creates a cookie on the screen 
    Draws it at location (x,y)
    
    Params
    x - the x-location of the centre
    y - the y-location of the centre"""
    baker_turtle.color(random.random(),random.random(), random.random())
    baker_turtle.fillcolor(random.random(),random.random(), random.random())
    baker_turtle.begin_fill()
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.circle(100)
    baker_turtle.end_fill()
    baker_turtle.penup()

    # Add chips
    baker_turtle.color("purple")
    baker_turtle.goto(2 + x, 2 + y)
    baker_turtle.stamp()

    # Add top right, bottom right, bottom left 
    baker_turtle.goto(10 + x, 10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(10 + x, -10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(-10 + x, -10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(-10 + x, 10 + y)
    baker_turtle.stamp()

# Create cookie
for _ in range(1000):
    offset_x= random.randint(-500, 501)
    offset_y= random.randint(-500, 501)

    make_cookie(offset_x, offset_y)


# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")






turtle.done()