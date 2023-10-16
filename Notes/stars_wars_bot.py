# Star Wars bot
# Kevin Wong
# October 16 2023

# Create a Star Wars bot that determines whether you're on the
# dark side or the light side

import time

# Intro
print("I will decide if you can join the Dark Side.")
time.sleep(1)

# Ask if the user likes red

red_like = input("Is red your favourite color?").lower().strip("!.,")
time.sleep(1)

#Ask if the user likes red
cape_like = input("Do you like capes?").lower().strip("!.,")
time.sleep(1)

#If the user answers yes to anything they're on the dark side
#If they answer no to all they're on the light side
if red_like == "yes" or cape_like == "yes":
    print("Dark side it is!")
else:
    print("Light side, I see.")


