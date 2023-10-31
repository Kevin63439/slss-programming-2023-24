# Pumpkin Drawing
# Author: Kevin Wong
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# Left Eye
carver.setposition(-30, 20)
carver.dot(30)

# Right Eye
carver.setposition(30, 20)
carver.dot(40,'blue')

#Shape
carver.penup()
carver.setposition(-200, 100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

#Ears
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

carver.pu()
carver.goto(-100,70)
carver.fillcolor('blue')
carver.begin_fill()
for _ in range(4):
    carver.forward(200)
    carver.left(90)
carver.end_fill()

# Mouth
carver.goto(-50,0)
carver.seth(270)
carver.pd()
carver.circle(50,180)

turtle.done()
