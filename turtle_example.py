# Turtle example
# Author: Kevin Wong
# Date: November 21 2023

import turtle

# Create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20
TURN_RIGHT = 90
TURN_LEFT = 90
# Make a turtle object
michaelangelo = turtle.Turtle()

# Get some input from the user
print("""To give commands, type
      F - to go forward
      L - to turn left
      R - to turn right.""")

# Repeat the below forever, or until the user says stop
done = False

while not done:
    command = input("Where should I go?")

    # Move the turtle around based on that input
    if command.strip(",.?! ").lower() == "f":
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command.strip(",.?!").lower() == "r":
        michaelangelo.right(TURN_RIGHT)
    elif command.strip(",.?!").lower() == "l":
        michaelangelo.left(TURN_LEFT)
    elif command == "stop":
        done = True

    